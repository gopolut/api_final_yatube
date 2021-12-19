from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import UserSerializer, PostSerializer, GroupSerializer, CommentSerializer, FollowSerializer
from .permissions import IsAuthorOrReadOnly, IsFollowerOrReadOnly
from posts.models import User, Group, Post, Comment, Follow


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthorOrReadOnly,)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = ('text', 'author', 'group', 'pub_date',)
    search_fields = ('text', 'author__username',) 
    ordering_fields = ('pub_date',)
    ordering = ('-pub_date',)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    # queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly, )
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = ('text', 'author',)
    search_fields = ('text', 'author__username',) 
    ordering_fields = ('created',)
    ordering = ('created',)

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        new_queryset = post.comments.all()
        return new_queryset

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = (IsFollowerOrReadOnly,) #(permissions.IsAuthenticatedOrReadOnly,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('user', 'following',)
    search_fields = ('user__username', 'following__username', )

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        new_queryset = user.follower.all()
        return new_queryset

    def perform_create(self, serializer):
        # following = self.kwargs.get('follow')
        # print('following', following)
        serializer.save(user=self.request.user)

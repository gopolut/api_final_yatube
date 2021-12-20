from django.shortcuts import get_object_or_404
from rest_framework import filters, viewsets
from rest_framework.pagination import LimitOffsetPagination

from django_filters.rest_framework import DjangoFilterBackend

from .permissions import IsAuthorOrReadOnly, IsFollowerOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer, UserSerializer)
from posts.models import Group, Post, User


class UserViewSet(viewsets.ReadOnlyModelViewSet):
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
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    filterset_fields = ('text', 'author', 'group', 'pub_date',)
    search_fields = ('text', 'author__username',)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly, )
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    filterset_fields = ('text', 'author',)
    search_fields = ('text', 'author__username',)

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        new_queryset = post.comments.all()
        return new_queryset

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = (IsFollowerOrReadOnly,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('user', 'following',)
    search_fields = ('user__username', 'following__username', )

    def get_queryset(self):
        new_queryset = self.request.user.follower.all()
        return new_queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

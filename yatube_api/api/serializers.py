from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


from posts.models import User, Group, Post, Comment, Follow


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'username', 'first_name', 'last_name', )
        model = User


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Group


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    # это поле обязательно указать, иначе запись не сохранится (ошибка: поле post обязательное)
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    # comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = CommentSerializer(many=True, required=False)

    class Meta:
        fields = ('id', 'text', 'author', 'group', 'image', 'pub_date',
                  'comments')
        model = Post


class FollowSerializer(serializers.ModelSerializer):
    # following = serializers.PrimaryKeyRelatedField(read_only=True)
    # following = serializers.SlugRelatedField(
    #     read_only=True, slug_field='username'
    # )
    # following = serializers.StringRelatedField(read_only=False)
    user = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    following = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    def validate(self, data):
        follower = self.context["request"].user
        following = data["following"]

        if Follow.objects.filter(user=follower, following=following).exists():
            raise serializers.ValidationError("Вы уже подписаны на данного автора")

        if follower == following:
            raise serializers.ValidationError("Вы не можете подписаться на самого себя")

        print('-data:', data['following'])
        return data
    

    class Meta:
        fields = ('id', 'user', 'following')
        model = Follow

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название сообщества'
    )
    slug = models.SlugField(
        unique=True,
        default='-пусто-',
        verbose_name='URL сообщества'
    )
    description = models.TextField(
        verbose_name='Описание сообщества'
    )

    def __str__(self) -> str:
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    image = models.ImageField(
        upload_to='posts/',
        null=True,
        blank=True
    )
    group = models.ForeignKey(
        Group,
        on_delete=SET_NULL,
        related_name='posts',
        null=True,
        blank=True,
        verbose_name='Сообщество'
    )

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True
    )

    def __str__(self) -> str:
        return f'Текст комментария: {self.text}'


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=CASCADE,
        related_name='follower',
        null=True,
        blank=True,
        verbose_name='Подписчик'
    )
    following = models.ForeignKey(
        User,
        on_delete=CASCADE,
        related_name='following',
        null=True,
        blank=True,
        verbose_name='Автор поста'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['following', 'user'],
                name='uniq_subscription'
            )
        ]

    def __str__(self) -> str:
        return f'Пользователь {self.user} подписан на {self.following}'

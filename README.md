![size](https://img.shields.io/github/languages/code-size/gopolut/api_final_yatube)
![django version](https://img.shields.io/pypi/pyversions/Django)

# Документация к API проекта Yatube (v1)

REST API для проекта **Yatube**. Социальная сеть для публикации личных дневников.

Проект **Yatube** - социальная сеть, которая позволяет вести свой собственный дневник (блог),
создавать сообщества, публиковать в них посты, подписываться на других авторов и комментировать их публикации.

> Для работы проекта необходим Python 3.8 и Django версии 2.2.16

API для сервиса **Yatube** позволяет:
+ работать с публикациями:
  + получать список всех публикаций
  + создавать публикации
  + обновлять публикации
  + удалять публикации

+ работать с комментариями к публикациям:
  + добавлять комментарии
  + получать комментарии
  + обновлять комментарии
  + удалять комментарии

+ Получать список сообществ
+ Подписываться на пользователей
+ Получать и обновлять JWT-токены

[Полная документация API (redoc.yaml)](https://github.com/gopolut/api_final_yatube/blob/master/yatube_api/static/redoc.yaml)

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/gopolut/api_final_yatube
cd kittygram
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
source env/bin/activate
```
Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

## Примеры работы с API

**GET-запрос** на получение списка всех публикаций:
'/api/v1/posts/'

```
{
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2021-10-14T20:41:29.648Z",
    "image": "string",
    "group": 0
}
```
**GET-запрос** на получение списка всех публикаций с указанием параметров limit и offset

`/api/v1/posts/?limit=2&offset=2`

Выдача с пагинацией:

```
{

    "count": 12,
    "next": "http://api.example.org/accounts/?offset=400&limit=100",
    "previous": "http://api.example.org/accounts/?offset=200&limit=100",
    "results": 

[

        {
            "id": 1,
            "author": "admin",
            "text": "Новый пост",
            "pub_date": "2021-10-14T20:41:29.648Z",
            "image": "new_image.gif",
            "group": 2
        }
    ]

}
```
**POST-запрос** на создание новой публикации:

`/api/v1/posts/'

```
{

    "text": "Новый пост",
    "image": "new_image.gif",
    "group": 2

}
```

Выдача:

```
{

    "id": 0,
    "author": "admin",
    "text": "Новый пост",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "new_image.gif",
    "group": 2

}
```

**POST-запрос** на добавление комментария к публикации

'/api/v1/posts/{post_id}/comments/'
```
{

    "text": "Комментарий к новому посту"

}
```

Выдача:

```
{

    "id": 3,
    "author": "admin",
    "text": "Комментарий к новому посту",
    "created": "2019-08-24T14:15:22Z",
    "post": 5

}
```

**Получение JWT-токена**

`/api/v1/jwt/create/`

```
{

    "username": "admin",
    "password": "password123"

}
```

// Выдача:

```
{
    "refresh": "string",
    "access": "string"
}
```
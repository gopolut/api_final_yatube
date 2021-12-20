https://img.shields.io/github/languages/code-size/gopolut/api_final_yatube
https://img.shields.io/pypi/pyversions/Django
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

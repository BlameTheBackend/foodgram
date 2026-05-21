# FoodGram

Foodgram — веб‑приложение для публикации рецептов, поиска блюд и формирования списка покупок.  
Пользователи могут создавать рецепты, просматривать рецепты других авторов, добавлять их в избранное, подписываться на авторов и формировать список покупок.

Проект состоит из:
- Backend: Django + Django REST Framework
- Frontend: React
- Инфраструктура: Docker, PostgreSQL, Gunicorn, nginx

Сайт проекта: http://yandexfoodgram.duckdns.org

## Основные возможности
- Для неавторизованных пользователей:
    - просмотр главной страницы с рецептами;
    - просмотр отдельных рецептов и страниц авторов;
    - фильтрация по тегам;
    - регистрация и авторизация.
- Для авторизованных пользователей:
    - создание, редактирование и удаление собственных рецептов;
    - добавление/удаление рецептов в избранное и в список покупок;
    - подписка/отписка на авторов, просмотр подписок;
    - скачивание списка покупок;
    - изменение пароля, выход из аккаунта.
- Для администратора:
    - управление пользователями, рецептами, ингредиентами и тегами;
    - доступ к админ‑панели Django.

## Стек технологий
- Backend: Python, Django, Django REST Framework, Djoser, PostgreSQL, Gunicorn  
- Frontend: JavaScript, React, CSS, HTML  
- Инфраструктура: Docker, Docker Compose, nginx, GitHub Actions, Docker Hub

## Структура проекта
```
foodgram/
├── .github/workflows/       # GitHub Actions
├── backend/                 # Backend-приложение Django
├── docs/                    # Документация API
├── frontend/                # Frontend-приложение React
├── nginx/                   # nginx конфигурация
├── README.md
```

## Переменные окружения
Создайте файл `.env` с обязательными переменными:
- POSTGRES_USER — имя пользователя PostgreSQL
- POSTGRES_PASSWORD — пароль PostgreSQL
- POSTGRES_DB — название базы данных
- DB_HOST — хост БД внутри Docker‑сети
- DB_PORT — порт PostgreSQL
- SECRET_KEY — секретный ключ Django
- DEBUG — режим отладки (True/False)
- ALLOWED_HOSTS — список разрешённых хостов

### Настройка секретов в GitHub
Добавьте в GitHub Secrets:
- DOCKERHUB_USERNAME
- DOCKERHUB_PASSWORD
- HOST (IP или домен сервера)
- USER (имя пользователя на сервере)
- SSH_KEY (приватный SSH ключ)
- POSTGRES_PASSWORD

После настройки при пуше в ветку `main` workflow:
- запускает тесты;
- собирает Docker‑образы и пушит на Docker Hub;
- подключается к серверу, обновляет контейнеры, применяет миграции и собирает статику.

## Работа с API
Документация доступна после запуска проекта:
http://foodgrammax.ddns.net/api/docs/

Основные эндпоинты:
- /api/users/ — пользователи
- /api/auth/token/login/ — получение токена
- /api/auth/token/logout/ — удаление токена
- /api/recipes/ — рецепты
- /api/recipes/{id}/ — отдельный рецепт
- /api/recipes/{id}/favorite/ — добавление/удаление из избранного
- /api/recipes/{id}/shopping_cart/ — добавление/удаление из списка покупок
- /api/recipes/download_shopping_cart/ — скачивание списка покупок
- /api/tags/ — теги
- /api/ingredients/ — ингредиенты
- /api/users/subscriptions/ — подписки
- /api/users/{id}/subscribe/ — подписка/отписка на автора

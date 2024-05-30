# Desafio Brasilprev

## O desafio é construir uma API REST, que possibilite executar as seguintes ações:

- Cadastro de cliente
- Cadastro de produto
- Contratação de plano
- Resgate de plano
- Aporte extra

## Stack que utilizei:

- Docker
- Python/Django
- PostgreSQL
- Scrapy
- Celery
- Django REST Framework

## Variáveis de ambiente

    DEBUG=True
    SECRET_KEY=arandomstring
    ALLOWED_HOSTS=*,
    DB_ENGINE=django.db.backends.postgresql
    DB_NAME=
    DB_USER=
    DB_PASSWORD=
    DB_HOST=db
    DB_PORT=5432
    RUN_PORT=8000
    RUN_HOST=0.0.0.0

## Comandos

    docker compose build
    docker compose up

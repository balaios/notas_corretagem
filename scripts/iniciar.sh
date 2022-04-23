#!/usr/bin/bash

psql -U postgres -c  "CREATE DATABASE notas_corretagem;"
psql -U postgres -d notas_corretagem -c "DROP TABLE public.alembic_version;"
psql -U postgres -d notas_corretagem -c "DROP TABLE public.notas_bmf CASCADE;"
psql -U postgres -d notas_corretagem -c "DROP TABLE public.notas_bovespa CASCADE;"
psql -U postgres -d notas_corretagem -c "DROP TABLE public.folhas_bmf CASCADE;"
psql -U postgres -d notas_corretagem -c "DROP TABLE public.folhas_bovespa CASCADE;"
psql -U postgres -d notas_corretagem -c "DROP TABLE public.operações_bmf CASCADE;"
psql -U postgres -d notas_corretagem -c "DROP TABLE public.operações_bovespa CASCADE;"
psql -U postgres -d notas_corretagem -c "DROP TABLE public.upload CASCADE;"


rm -rf migrations
export FLASK_APP=notas_corretagem
export FLASK_ENV=development
flask db init
flask db migrate
flask db upgrade
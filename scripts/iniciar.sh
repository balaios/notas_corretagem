#!/usr/bin/bash

psql -U postgres -c  "CREATE DATABASE notas_corretagem;"
psql -U postgres -d notas_corretagem -c "DROP TABLE public.alembic_version;"
psql -U postgres -d notas_corretagem -c "DROP TABLE public.nota_bmf CASCADE;"
psql -U postgres -d notas_corretagem -c "DROP TABLE public.nota_bovespa CASCADE;"
psql -U postgres -d notas_corretagem -c "DROP TABLE public.folha_bmf CASCADE;"
psql -U postgres -d notas_corretagem -c "DROP TABLE public.operacao_bmf CASCADE;"
psql -U postgres -d notas_corretagem -c "DROP TABLE public.operacao_bovespa CASCADE;"
psql -U postgres -d notas_corretagem -c "DROP TABLE public.upload CASCADE;"


rm -rf migrations
export FLASK_APP=notas_corretagem
export FLASK_ENV=development
flask db init
flask db migrate
flask db upgrade
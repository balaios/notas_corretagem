#!/usr/bin/bash

psql -U postgres -d notas -c "DROP TABLE public.alembic_version;"
psql -U postgres -d notas -c "DROP TABLE public.folhasbmf CASCADE;"
psql -U postgres -d notas -c "DROP TABLE public.folhasbovespa CASCADE;"
psql -U postgres -d notas -c "DROP TABLE public.notasbmf CASCADE;"
psql -U postgres -d notas -c "DROP TABLE public.notasbovespa CASCADE;"
psql -U postgres -d notas -c "DROP TABLE public.operaçõesbmf CASCADE;"
psql -U postgres -d notas -c "DROP TABLE public.operaçõesbovespa CASCADE;"
psql -U postgres -d notas -c "DROP TABLE public.upload CASCADE;"


rm -rf migrations
export FLASK_APP=notas_corretagem
export FLASK_ENV=development
flask db init
flask db migrate
flask db upgrade
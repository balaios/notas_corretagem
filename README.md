# Notas de Corretagem 
## Ler as notas de corretagem em PDF que estão no padrão SINACOR

O programa usa a biblioteca PDFMiner.six para extrair o conteudo das páginas junto com seus eixos x/y. Filtra esses dados com posicões já definidas e salva num banco de dados PostgreSQL.

Python-PDFMiner-Flask-SQLAlchemy.

## Instalação

Instalando as dependências.

```sh
pip install requirements.txt
```

## Executar

Para iniciar o banco de dados:
```sh
export FLASK_APP=notas_corretagem
flask db init
flask db migrate
flask db upgrade
```

Executar o flask:

```sh
export FLASK_APP=notas_corretagem
flask run
```

Acessivel pela porta padrão do flask.

```sh
127.0.0.1:5000
```

## Licença

Licença Pública Geral GNU v2.0

**Meu primeiro programa em Python!**

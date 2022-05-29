from flask import Blueprint, render_template

from ..models.bovespa import FolhaBovespa, OperacaoBovespa


bovespa = Blueprint("bovespa", __name__)


@bovespa.get("/operacoesb3")
def operacaob3():

    operacoes = OperacaoBovespa.query.all()

    return render_template("bovespa/operaçõesb3.html", operacoes=operacoes)


@bovespa.get("/resumob3")
def resumob3():

    folhas = FolhaBovespa.query.all()

    return render_template("bovespa/resumob3.html", folhas=folhas)

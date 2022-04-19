from flask import Blueprint, render_template

from ..models.bovespa import FolhasBovespa, OperaçõesBovespa


bovespa = Blueprint("bovespa", __name__)


@bovespa.get("/operacoesb3")
def operacaob3():

    operações = OperaçõesBovespa.query.all()

    return render_template("bovespa/operaçõesb3.html", operações=operações)


@bovespa.get("/resumob3")
def resumob3():

    folhas = FolhasBovespa.query.all()

    return render_template("bovespa/resumob3.html", folhas=folhas)

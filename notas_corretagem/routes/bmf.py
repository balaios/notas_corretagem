from flask import Blueprint, render_template

from ..models.bmf import NotaBmf, OperacaoBmf

bmf = Blueprint("bmf", __name__)


@bmf.get("/operacoesbmf")
def operacaobmf():

    operacoes = OperacaoBmf.query.all()

    return render_template("bmf/operaçõesbmf.html", operacoes=operacoes)


@bmf.get("/resumobmf")
def resumobmf():

    notas = NotaBmf.query.all()

    return render_template("bmf/resumobmf.html", notas=notas)

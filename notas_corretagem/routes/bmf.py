from flask import Blueprint, render_template

from ..models.bmf import FolhasBmf, OperaçõesBmf

bmf = Blueprint("bmf", __name__)


@bmf.get("/operacoesbmf")
def operacaobmf():

    operações = OperaçõesBmf.query.all()

    return render_template("bmf/operaçõesbmf.html", operações=operações)


@bmf.get("/resumobmf")
def resumobmf():

    folhas = FolhasBmf.query.all()

    return render_template("bmf/resumobmf.html", folhas=folhas)

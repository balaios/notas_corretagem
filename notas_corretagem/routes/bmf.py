from flask import Blueprint, render_template

from ..models.bmf import FolhaBmf, OperacaoBmf

bmf = Blueprint("bmf", __name__)


@bmf.get("/operacoesbmf")
def operacaobmf():

    operações = OperacaoBmf.query.all()

    return render_template("bmf/operaçõesbmf.html", operações=operações)


@bmf.get("/totalbmf")
def totalbmf():

    operacoes = OperacaoBmf.query.all()
    compra = 0
    venda = 0
    taxa_registro = 0
    emolumentos = 0
    for operacao in operacoes:
        if operacao.cv == "C":
            compra += int(operacao.quantidade) * float(operacao.preco_ajuste)
            emolumentos += int(operacao.quantidade) * 0.08
            taxa_registro += int(operacao.quantidade) * 0.16
        else:
            venda += int(operacao.quantidade) * float(operacao.preco_ajuste)
            emolumentos += int(operacao.quantidade) * 0.08
            taxa_registro += int(operacao.quantidade) * 0.16

    taxa_registro = round(taxa_registro, 2)
    emolumentos = round(emolumentos, 2)
    valor_dos_negocios = (venda - compra) / 5
    total = valor_dos_negocios + (-(emolumentos + taxa_registro))

    return render_template("bmf/totalbmf.html", valor_dos_negocios=valor_dos_negocios, taxa_registro=taxa_registro, emolumentos=emolumentos, total=total)


@bmf.get("/resumobmf")
def resumobmf():

    folhas = FolhaBmf.query.all()

    return render_template("bmf/resumobmf.html", folhas=folhas)

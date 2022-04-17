from flask import Blueprint, redirect, render_template, request, url_for

from ..extensions import db
from ..forms.upload import Pdf
from ..models.bmf import Folhasbmf, Notasbmf, Operaçõesbmf
from ..models.bovespa import Folhasbovespa, Notasbovespa, Operaçõesbovespa
from ..models.upload import Upload
from ..pdf import principal

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/add", methods=["GET", "POST"])
def add():

    form = Pdf(meta={'csrf': False})

    if form.validate_on_submit():
        pdfs = form.pdfs.data
        for pdf in pdfs:
            pdf.save("notas_corretagem/uploads/" + pdf.filename)
            principal("notas_corretagem/uploads/" + pdf.filename)
            upload = Upload(filename=pdf.filename)
            db.session.add(upload)
            db.session.commit()

        return redirect(url_for("main.sucesso"))
    return render_template("upload.html", form=form)


@main.route("/declaracao")
def declaração():

    bovespa = Notasbovespa.query.all()
    bmf = Notasbmf.query.all()
    notas = bmf + bovespa

    anos = set()
    for nota in notas:
        anos.add(nota.data_pregão.split("/")[2])

    return render_template("declaracao.html", anos=anos)


@main.route("/operacoesbmf")
def operacaobmf():

    operações = Operaçõesbmf.query.all()

    return render_template("bmf/operaçõesbmf.html", operações=operações)


@main.route("/resumobmf")
def resumobmf():

    folhas = Folhasbmf.query.all()

    return render_template("bmf/resumobmf.html", folhas=folhas)


@main.route("/operacoesb3")
def operacaob3():

    operações = Operaçõesbovespa.query.all()

    return render_template("bovespa/operaçõesb3.html", operações=operações)


@main.route("/resumob3")
def resumob3():

    folhas = Folhasbovespa.query.all()

    return render_template("bovespa/resumob3.html", folhas=folhas)


@main.route("/sucesso")
def sucesso():
    return render_template("sucesso.html")

from flask import Blueprint, redirect, render_template, request, url_for

from ..extensions import db
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
    if request.method == "POST":
        pdfs = request.files.getlist("files[]")
        if not pdfs:
            return redirect(url_for("main.add"))
        for pdf in pdfs:
            pdf.save("notas_corretagem/uploads/" + pdf.filename)
            principal("notas_corretagem/uploads/" + pdf.filename)
            upload = Upload(filename=pdf.filename)
            db.session.add(upload)
            db.session.commit()

        return redirect(url_for("main.sucesso"))
    return render_template("add.html")


@main.route("/operacoesbmf")
def operacaobmf():

    messages = Operaçõesbmf.query.join(Folhasbmf).join(Notasbmf).all()

    return render_template("operaçõesbmf.html", messages=messages)


@main.route("/resumobmf")
def resumobmf():

    messages = Folhasbmf.query.all()

    return render_template("resumobmf.html", messages=messages)


@main.route("/operacoesb3")
def operacaob3():

    messages = Operaçõesbovespa.query.join(Folhasbovespa).join(Notasbovespa).all()

    return render_template("operaçõesb3.html", messages=messages)


@main.route("/resumob3")
def resumob3():

    messages = Folhasbovespa.query.all()

    return render_template("resumob3.html", messages=messages)


@main.route("/sucesso")
def sucesso():
    return render_template("sucesso.html")

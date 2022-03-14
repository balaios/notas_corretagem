from flask import Blueprint, redirect, render_template, request, url_for

from ..extensions import db
from ..models.bmf import Folhasbmf, Operaçõesbmf
from ..models.bovespa import Folhasb3, Operaçõesb3
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

    messages = Operaçõesbmf.query.all()

    return render_template("operaçõesbmf.html", messages=messages)


@main.route("/resumobmf")
def resumobmf():

    messages = Folhasbmf.query.all()

    return render_template("resumobmf.html", messages=messages)


@main.route("/operacoesb3")
def operacaob3():

    messages = Operaçõesb3.query.all()

    return render_template("operaçõesb3.html", messages=messages)


@main.route("/resumob3")
def resumob3():

    messages = Folhasb3.query.all()

    return render_template("resumob3.html", messages=messages)


@main.route("/sucesso")
def sucesso():
    return render_template("sucesso.html")

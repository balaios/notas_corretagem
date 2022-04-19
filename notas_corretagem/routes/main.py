from flask import Blueprint, redirect, render_template, url_for

from ..extensions import db
from ..forms.upload import Pdf
from ..models.upload import Upload
from ..pdf import principal

main = Blueprint("main", __name__)


@main.get("/")
def index():
    return render_template("index.html")


@main.get("/add")
def add():

    form = Pdf(meta={'csrf': False})

    return render_template("upload.html", form=form)


@main.post("/add")
def valid_pdf():

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


@main.get("/sucesso")
def sucesso():
    return render_template("sucesso.html")

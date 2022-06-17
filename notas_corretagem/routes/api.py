from flask import Blueprint, jsonify, request

from ..extensions import db
from ..models.bmf import NotaBmf, OperacaoBmf
from ..models.bovespa import NotaBovespa, OperacaoBovespa
from ..models.upload import Upload
from ..pdf import ler_pdf
from ..schemas.bmf import NotaBmfSchema, OperacaoBmfSchema
from ..schemas.bovespa import NotaBovespaSchema, OperacaoBovespaSchema

api = Blueprint("api", __name__, url_prefix="/api")


@api.get("/")
def index():
    return jsonify({"hello": "world"})


@api.post("/add/")
def add():
    pdfs = request.files.getlist("pdfs")
    for pdf in pdfs:
        pdf.save("notas_corretagem/uploads/" + pdf.filename)
        ler_pdf("notas_corretagem/uploads/" + pdf.filename)
        upload = Upload(filename=pdf.filename)
        db.session.add(upload)
        db.session.commit()

    return jsonify({"status": "ok"})


@api.get("/operacoesbmf/")
def operacaobmf():

    operacoes = OperacaoBmf.query.all()

    schema = OperacaoBmfSchema(many=True)
    data = schema.dump(operacoes)

    return jsonify({"data": data})


@api.get("/resumobmf/")
def resumobmf():

    folhas = NotaBmf.query.all()

    schema = NotaBmfSchema(many=True)
    data = schema.dump(folhas)

    return jsonify({"data": data})


@api.get("/operacoesb3/")
def operacaob3():

    operacoes = OperacaoBovespa.query.all()

    schema = OperacaoBovespaSchema(many=True)
    data = schema.dump(operacoes)

    return jsonify({"data": data})


@api.get("/resumob3/")
def resumob3():

    folhas = NotaBovespa.query.all()

    schema = NotaBovespaSchema(many=True)
    data = schema.dump(folhas)

    return jsonify({"data": data})

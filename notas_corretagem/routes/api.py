from flask import Blueprint, jsonify, request

from ..extensions import db
from ..models.bmf import Folhasbmf, Notasbmf, Operaçõesbmf
from ..models.bovespa import Folhasbovespa, Notasbovespa, Operaçõesbovespa
from ..models.upload import Upload
from ..pdf import principal
from ..schemas.bmf import FolhasbmfSchema, NotasbmfSchema, OperaçõesbmfSchema
from ..schemas.bovespa import (FolhasbovespaSchema, NotasbovespaSchema,
                               OperaçõesbovespaSchema)

api = Blueprint("api", __name__, url_prefix="/api")


@api.route("/")
def index():
    return jsonify({"hello": "world"})


@api.route("/add", methods=["POST"])
def add():
    pdfs = request.files.getlist("files[]")
    for pdf in pdfs:
        pdf.save("notas_corretagem/uploads/" + pdf.filename)
        principal("notas_corretagem/uploads/" + pdf.filename)
        upload = Upload(filename=pdf.filename)
        db.session.add(upload)
        db.session.commit()

    return jsonify({"status": "ok"})


@api.route("/operacoesbmf")
def operacaobmf():

    messages = Operaçõesbmf.query.join(Folhasbmf).join(Notasbmf).all()

    operacoesbmf_schema = OperaçõesbmfSchema(many=True)
    data = operacoesbmf_schema.dump(messages)

    return jsonify({"data": data})


@api.route("/resumobmf")
def resumobmf():

    messages = Operaçõesbmf.query.join(Folhasbmf).join(Notasbmf).all()

    operacoesbmf_schema = OperaçõesbmfSchema(many=True)
    data = operacoesbmf_schema.dump(messages)

    return jsonify({"data": data})


@api.route("/operacoesb3")
def operacaob3():

    messages = Operaçõesbmf.query.join(Folhasbmf).join(Notasbmf).all()

    operacoesbmf_schema = OperaçõesbmfSchema(many=True)
    data = operacoesbmf_schema.dump(messages)

    return jsonify({"data": data})


@api.route("/resumob3")
def resumob3():

    messages = Operaçõesbmf.query.join(Folhasbmf).join(Notasbmf).all()

    operacoesbmf_schema = OperaçõesbmfSchema(many=True)
    data = operacoesbmf_schema.dump(messages)

    return jsonify({"data": data})



from flask import Blueprint, jsonify, request

from ..extensions import db
from ..models.bmf import FolhasBmf, OperaçõesBmf
from ..models.bovespa import FolhasBovespa, OperaçõesBovespa
from ..models.upload import Upload
from ..pdf import principal
from ..schemas.bmf import OperaçõesBmfSchema, FolhasBmfSchema
from ..schemas.bovespa import OperaçõesBovespaSchema, FolhasBovespaSchema

api = Blueprint("api", __name__, url_prefix="/api")


@api.get("/")
def index():
    return jsonify({"hello": "world"})


@api.post("/add/")
def add():
    pdfs = request.files.getlist("pdfs")
    for pdf in pdfs:
        pdf.save("notas_corretagem/uploads/" + pdf.filename)
        principal("notas_corretagem/uploads/" + pdf.filename)
        upload = Upload(filename=pdf.filename)
        db.session.add(upload)
        db.session.commit()

    return jsonify({"status": "ok"})


@api.get("/operacoesbmf/")
def operacaobmf():

    operações = OperaçõesBmf.query.all()

    schema = OperaçõesBmfSchema(many=True)
    data = schema.dump(operações)

    return jsonify({"data": data})


@api.get("/resumobmf/")
def resumobmf():

    folhas = FolhasBmf.query.all()

    schema = FolhasBmfSchema(many=True)
    data = schema.dump(folhas)

    return jsonify({"data": data})


@api.get("/operacoesb3/")
def operacaob3():

    operações = OperaçõesBovespa.query.all()

    schema = OperaçõesBovespaSchema(many=True)
    data = schema.dump(operações)

    return jsonify({"data": data})


@api.get("/resumob3/")
def resumob3():

    folhas = FolhasBovespa.query.all()

    schema = FolhasBovespaSchema(many=True)
    data = schema.dump(folhas)

    return jsonify({"data": data})

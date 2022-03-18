from ..extensions import db


class Notasbmf(db.Model):
    __tablename__ = "notasbmf"
    id = db.Column(db.Integer, primary_key=True)
    número_corretora = db.Column(db.String(40))
    nr_nota = db.Column(db.String(40))
    data_pregão = db.Column(db.String(40))
    cnpj_cpf = db.Column(db.String(40))
    código_cliente = db.Column(db.String(40))
    folha = db.relationship("Folhasbmf", backref="notasbmf", lazy=True)


class Folhasbmf(db.Model):
    __tablename__ = "folhasbmf"
    id = db.Column(db.Integer, primary_key=True)
    notasbmf_id = db.Column(db.Integer, db.ForeignKey("notasbmf.id"))
    folha = db.Column(db.String(40))
    venda_disponível = db.Column(db.String(40))
    compra_disponível = db.Column(db.String(40))
    venda_opções = db.Column(db.String(40))
    compra_opções = db.Column(db.String(40))
    valor_negócios = db.Column(db.String(40))
    irrf = db.Column(db.String(40))
    irrf_day_trade_proj = db.Column(db.String(40))
    taxa_operacional = db.Column(db.String(40))
    taxas_bmf = db.Column(db.String(40))
    taxa_registro_bmf = db.Column(db.String(40))
    outros_custos = db.Column(db.String(40))
    impostos = db.Column(db.String(40))
    ajuste_posição = db.Column(db.String(40))
    ajuste_day_trade = db.Column(db.String(40))
    total_despesas = db.Column(db.String(40))
    outros = db.Column(db.String(40))
    irrf_operacional = db.Column(db.String(40))
    total_conta_investimento = db.Column(db.String(40))
    total_conta_normal = db.Column(db.String(40))
    total_líquido = db.Column(db.String(40))
    total_líquido_nota = db.Column(db.String(40))
    operaçõesbmf = db.relationship("Operaçõesbmf", backref="folhasbmf", lazy=True)


class Operaçõesbmf(db.Model):
    __tablename__ = "operaçõesbmf"
    id = db.Column(db.Integer, primary_key=True)
    folhasbmf_id = db.Column(db.Integer, db.ForeignKey("folhasbmf.id"))
    cv = db.Column(db.String(40))
    mercadoria = db.Column(db.String(40))
    vencimento = db.Column(db.String(40))
    quantidade = db.Column(db.String(40))
    preço_ajuste = db.Column(db.String(40))
    tipo_negócio = db.Column(db.String(20), default=0)
    valor_operação = db.Column(db.String(40))
    dc = db.Column(db.String(40))
    taxa_operacional = db.Column(db.String(40))

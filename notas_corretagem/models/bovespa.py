from ..extensions import db


class Notasbovespa(db.Model):
    __tablename__ = "notas_bovespa"

    id = db.Column(db.Integer, primary_key=True)
    número_corretora = db.Column(db.String(40))
    nr_nota = db.Column(db.String(40))
    data_pregão = db.Column(db.String(40))
    cnpj_cpf = db.Column(db.String(40))
    código_cliente = db.Column(db.String(40))
    debêntures = db.Column(db.String(40))
    folhas_bovespa = db.relationship("Folhasbovespa", backref="notas_bovespa", lazy=True)


class Folhasbovespa(db.Model):
    __tablename__ = "folhas_bovespa"

    id = db.Column(db.Integer, primary_key=True)
    notas_id = db.Column(db.Integer, db.ForeignKey("notas_bovespa.id"))
    folha = db.Column(db.String(40))
    debêntures = db.Column(db.String(40))
    vendas_vista = db.Column(db.String(40))
    compras_vista = db.Column(db.String(40))
    compra_opções = db.Column(db.String(40))
    venda_opções = db.Column(db.String(40))
    operações_termo = db.Column(db.String(40))
    valor_operações_títulos_públ = db.Column(db.String(40))
    valor_operações = db.Column(db.String(40))
    valor_líquido_operações = db.Column(db.String(40))
    taxa_liquidação = db.Column(db.String(40))
    taxa_registro = db.Column(db.String(40))
    total_clbc = db.Column(db.String(40))
    taxa_termo_opções = db.Column(db.String(40))
    taxa_ana = db.Column(db.String(40))
    emolumentos = db.Column(db.String(40))
    total_bovespa = db.Column(db.String(40))
    taxa_operacional = db.Column(db.String(40))
    execução = db.Column(db.String(40))
    taxa_custódia = db.Column(db.String(40))
    impostos = db.Column(db.String(40))
    irrf = db.Column(db.String(40))
    outros = db.Column(db.String(40))
    total_custos_despesas = db.Column(db.String(40))
    líquido = db.Column(db.String(40))
    operações_bovespa = db.relationship(
        "Operaçõesbovespa", backref="folhas_bovespa", lazy=True
    )


class Operaçõesbovespa(db.Model):
    __tablename__ = "operações_bovespa"

    id = db.Column(db.Integer, primary_key=True)
    folhas_id = db.Column(db.Integer, db.ForeignKey("folhas_bovespa.id"))
    q = db.Column(db.String(40))
    negociação = db.Column(db.String(40))
    cv = db.Column(db.String(40))
    tipo_mercado = db.Column(db.String(40))
    prazo = db.Column(db.String(40))
    especificação_título = db.Column(db.String(40))
    obs = db.Column(db.String(40))
    quantidade = db.Column(db.String(40))
    preço_ajuste = db.Column(db.String(40))
    valor_operação = db.Column(db.String(40))
    dc = db.Column(db.String(40))

from ..extensions import db


class NotaBmf(db.Model):
    __tablename__ = "nota_bmf"

    id = db.Column(db.Integer, primary_key=True)
    numero_corretora = db.Column(db.String(40))
    nr_nota = db.Column(db.String(40))
    data_pregao = db.Column(db.Date)
    cnpj_cpf = db.Column(db.String(40))
    codigo_cliente = db.Column(db.String(40))
    folhas_bmf = db.relationship("FolhaBmf", backref="nota_bmf", lazy=True)


class FolhaBmf(db.Model):
    __tablename__ = "folha_bmf"

    id = db.Column(db.Integer, primary_key=True)
    nota_id = db.Column(db.Integer, db.ForeignKey("nota_bmf.id"))
    folha = db.Column(db.String(40))
    venda_disponivel = db.Column(db.String(40))
    compra_disponivel = db.Column(db.String(40))
    venda_opcoes = db.Column(db.String(40))
    compra_opcoes = db.Column(db.String(40))
    valor_negocios = db.Column(db.String(40))
    irrf = db.Column(db.String(40))
    irrf_day_trade_proj = db.Column(db.String(40))
    taxa_operacional = db.Column(db.String(40))
    taxas_bmf = db.Column(db.String(40))
    taxa_registro_bmf = db.Column(db.String(40))
    outros_custos = db.Column(db.String(40))
    impostos = db.Column(db.String(40))
    ajuste_posicao = db.Column(db.String(40))
    ajuste_day_trade = db.Column(db.String(40))
    total_despesas = db.Column(db.String(40))
    outros = db.Column(db.String(40))
    irrf_operacional = db.Column(db.String(40))
    total_conta_investimento = db.Column(db.String(40))
    total_conta_normal = db.Column(db.String(40))
    total_liquido = db.Column(db.String(40))
    total_liquido_nota = db.Column(db.String(40))
    operacoes_bmf = db.relationship("OperacaoBmf", backref="folha_bmf", lazy=False)


class OperacaoBmf(db.Model):
    __tablename__ = "operacao_bmf"

    id = db.Column(db.Integer, primary_key=True)
    folha_id = db.Column(db.Integer, db.ForeignKey("folha_bmf.id"))
    cv = db.Column(db.String(40))
    mercadoria = db.Column(db.String(40))
    vencimento = db.Column(db.String(40))
    quantidade = db.Column(db.String(40))
    preco_ajuste = db.Column(db.String(40))
    tipo_negocio = db.Column(db.String(20))
    valor_operacao = db.Column(db.String(40))
    dc = db.Column(db.String(40))
    taxa_operacional = db.Column(db.String(40))
    preco_medio_compra = db.Column(db.Float, default=0.0)
    preco_medio_venda = db.Column(db.Float, default=0.0)

from ..extensions import db


class NotaBovespa(db.Model):
    __tablename__ = "nota_bovespa"

    id = db.Column(db.Integer, primary_key=True)
    numero_corretora = db.Column(db.String(40))
    nr_nota = db.Column(db.String(40))
    data_pregao = db.Column(db.Date)
    cnpj_cpf = db.Column(db.String(40))
    codigo_cliente = db.Column(db.String(40))
    debentures = db.Column(db.String(40))
    vendas_vista = db.Column(db.String(40))
    compras_vista = db.Column(db.String(40))
    compra_opcoes = db.Column(db.String(40))
    venda_opcoes = db.Column(db.String(40))
    operacoes_termo = db.Column(db.String(40))
    valor_op_titulos_publ = db.Column(db.String(40))
    valor_operacoes = db.Column(db.String(40))
    irrf_day_trade = db.Column(db.String(40))
    irrf_projecao = db.Column(db.String(40))
    valor_liquido_operacoes = db.Column(db.String(40))
    taxa_liquidacao = db.Column(db.String(40))
    taxa_registro = db.Column(db.String(40))
    total_clbc = db.Column(db.String(40))
    taxa_termo_opcoes = db.Column(db.String(40))
    taxa_ana = db.Column(db.String(40))
    emolumentos = db.Column(db.String(40))
    total_bovespa = db.Column(db.String(40))
    taxa_operacional = db.Column(db.String(40))
    execucao = db.Column(db.String(40))
    taxa_custodia = db.Column(db.String(40))
    impostos = db.Column(db.String(40))
    irrf = db.Column(db.String(40))
    outros = db.Column(db.String(40))
    total_custos_despesas = db.Column(db.String(40))
    liquido = db.Column(db.String(40))
    folha_bovespa = db.relationship(
        "OperacaoBovespa", backref="nota_bovespa", lazy=True
    )


class OperacaoBovespa(db.Model):
    __tablename__ = "operacao_bovespa"

    id = db.Column(db.Integer, primary_key=True)
    nota_id = db.Column(db.Integer, db.ForeignKey("nota_bovespa.id"))
    folha = db.Column(db.String(40))
    q = db.Column(db.String(40))
    negociacao = db.Column(db.String(40))
    cv = db.Column(db.String(40))
    tipo_mercado = db.Column(db.String(40))
    prazo = db.Column(db.String(40))
    especificacao_titulo = db.Column(db.String(40))
    obs = db.Column(db.String(40))
    quantidade = db.Column(db.String(40))
    preco_ajuste = db.Column(db.String(40))
    valor_operacao = db.Column(db.String(40))
    dc = db.Column(db.String(40))

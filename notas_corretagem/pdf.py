from pdfminer.high_level import extract_pages
from pdfminer.layout import LAParams, LTTextBoxHorizontal

from .extensions import db
from .models.bmf import NotaBmf, OperacaoBmf
from .models.bovespa import NotaBovespa, OperacaoBovespa

nota_bmf = {
    "numero_corretora": (480, 520, 90, 110),
    "nr_nota": (450, 490, 50, 70),
    "data_pregao": (520, 570, 50, 70),
    "cnpj_cpf": (460, 550, 130, 150),
    "codigo_cliente": (460, 550, 150, 170),
    "venda_disponivel": (110, 140, 630, 655),
    "compra_disponivel": (200, 250, 630, 655),
    "venda_opcoes": (330, 360, 630, 655),
    "compra_opcoes": (430, 470, 630, 655),
    "valor_negocios": (510, 590, 630, 655),
    "irrf": (110, 140, 650, 675),
    "irrf_day_trade_proj": (220, 250, 650, 675),
    "taxa_operacional": (280, 360, 650, 675),
    "taxas_bmf": (500, 570, 650, 675),
    "taxa_registro_bmf": (400, 480, 650, 675),
    "outros_custos": (170, 190, 675, 700),
    "impostos": (210, 250, 675, 700),
    "ajuste_posicao": (280, 350, 675, 700),
    "ajuste_day_trade": (390, 460, 675, 700),
    "total_despesas": (540, 570, 675, 700),
    "outros": (50, 90, 700, 720),
    "irrf_operacional": (110, 150, 700, 720),
    "total_conta_investimento": (200, 250, 700, 720),
    "total_conta_normal": (310, 350, 700, 720),
    "total_liquido": (420, 460, 700, 720),
    "total_liquido_nota": (500, 600, 700, 720),
}

operacao_bmf = {
    "folha": (490, 520, 50, 70),
    "cv": (30, 50, 182, 600),
    "mercadoria": (45, 90, 182, 600),
    "vencimento": (110, 160, 182, 600),
    "quantidade": (200, 230, 182, 600),
    "preco_ajuste": (230, 285, 182, 600),
    "tipo_negocio": (285, 370, 182, 600),
    "valor_operacao": (380, 460, 182, 600),
    "dc": (460, 480, 182, 600),
    "taxa_operacional": (540, 570, 182, 600),
}

nota_bovespa = {
    "numero_corretora": (440, 500, 160, 180),
    "nr_nota": (435, 470, 50, 70),
    "data_pregao": (520, 570, 50, 70),
    "cnpj_cpf": (420, 480, 140, 160),
    "codigo_cliente": (35, 70, 140, 160),
    "debentures": (200, 300, 455, 475),
    "vendas_vista": (200, 300, 465, 485),
    "compras_vista": (200, 300, 475, 495),
    "compra_opcoes": (200, 300, 485, 505),
    "venda_opcoes": (200, 300, 495, 510),
    "operacoes_termo": (200, 300, 505, 520),
    "valor_op_titulos_publ": (200, 300, 515, 525),
    "valor_operacoes": (200, 300, 525, 545),
    "irrf_day_trade": (30, 300, 610, 640),
    "irrf_projecao": (30, 300, 610, 640),
    "valor_liquido_operacoes": (450, 560, 465, 480),
    "taxa_liquidacao": (450, 560, 475, 490),
    "taxa_registro": (450, 560, 485, 500),
    "total_clbc": (450, 560, 495, 506),
    "taxa_termo_opcoes": (450, 560, 510, 525),
    "taxa_ana": (450, 560, 525, 535),
    "emolumentos": (450, 560, 530, 545),
    "total_bovespa": (450, 560, 540, 555),
    "taxa_operacional": (450, 560, 565, 580),
    "execucao": (450, 560, 575, 590),
    "taxa_custodia": (450, 560, 585, 600),
    "impostos": (450, 560, 595, 610),
    "irrf": (450, 560, 605, 620),
    "outros": (450, 560, 615, 630),
    "total_custos_despesas": (450, 560, 625, 640),
    "liquido": (450, 560, 635, 655),
}

operacao_bovespa = {
    "folha": (490, 520, 50, 70),
    "q": (30, 45, 250, 450),
    "negociacao": (40, 80, 250, 450),
    "cv": (90, 110, 250, 450),
    "tipo_mercado": (105, 160, 250, 450),
    "prazo": (170, 188, 250, 450),
    "especificacao_titulo": (185, 300, 250, 450),
    "obs": (300, 340, 250, 450),
    "quantidade": (330, 390, 250, 450),
    "preco_ajuste": (390, 450, 250, 450),
    "valor_operacao": (450, 550, 250, 450),
    "dc": (545, 560, 250, 450),
}


tipo = {
    "BMF": {
        "cabecalho": nota_bmf,
        "operacao": operacao_bmf,
        "nota_db": NotaBmf,
        "operacao_db": OperacaoBmf,
    },
    "BOVESPA": {
        "cabecalho": nota_bovespa,
        "operacao": operacao_bovespa,
        "nota_db": NotaBovespa,
        "operacao_db": OperacaoBovespa,
    },
}


def ler_pdf(arquivo_pdf):
    laparams = LAParams(char_margin=0.5, line_margin=0.0)
    for layout in extract_pages(arquivo_pdf, laparams=laparams):
        bbox_texto = criar_bbox_texto(layout)
        tipo_nota = verificar_tipo_da_nota(bbox_texto)
        nota = seleciona_textos_nota(bbox_texto, tipo_nota, "cabecalho")
        operacao = seleciona_textos_nota(bbox_texto, tipo_nota, "operacao")
        tratar_texto(nota)
        inserir_banco_de_dados(nota, operacao, tipo_nota)


def criar_bbox_texto(layout):
    bbox_texto = {}
    for obj in layout._objs:
        if isinstance(obj, LTTextBoxHorizontal):
            x0, y1, x1, y0 = obj.bbox
            bbox_texto[
                int(x0),
                int(x1),
                int(layout.y1 - y0),
                int(layout.y1 - y1),
            ] = obj.get_text().strip()
    return bbox_texto


def verificar_tipo_da_nota(layout):
    for obj in layout.values():
        if "BM&F" in obj:
            return "BMF"
        if "BOVESPA" in obj:
            return "BOVESPA"
    return "Não encontrado"


def seleciona_textos_nota(dicionario_bbox_texto, tipo_nota, extra):
    textos_da_nota = {}
    folha = 0
    posicoes_textos = tipo[tipo_nota][extra]
    for bbox, texto in dicionario_bbox_texto.items():
        for campo, bboxmodelo in posicoes_textos.items():
            if (
                bbox[0] >= bboxmodelo[0]
                and bbox[1] <= bboxmodelo[1]
                and bbox[2] >= bboxmodelo[2]
                and bbox[3] <= bboxmodelo[3]
            ):
                if "cv" in posicoes_textos:
                    linha = bbox[3]
                    if campo == "folha":
                        folha = texto
                    elif linha in textos_da_nota:
                        textos_da_nota[linha][campo] = texto
                    else:
                        textos_da_nota[linha] = {}
                        textos_da_nota[linha][campo] = texto
                        textos_da_nota[linha]["folha"] = folha
                else:
                    if textos_da_nota.get(campo):
                        textos_da_nota[campo] += " " + texto
                    else:
                        textos_da_nota[campo] = texto
    return textos_da_nota


def tratar_texto(conteudo):
    for chave, texto in conteudo.items():
        if isinstance(texto, dict):
            tratar_texto(texto)
        else:
            texto = (
                texto.replace("|", "")
                .replace(".", "")
                .replace(",", ".")
                .replace("    ", "")
                .replace("-", "")
                .strip()
            )
            if chave == "irrf_day_trade":
                conteudo[chave] = texto.split(" ")[5]
            elif chave == "irrf_projecao":
                conteudo[chave] = texto.split(" ")[-1]
            elif "D" in texto or "C" in texto:
                if "D" in texto:
                    conteudo[chave] = str(float(texto.replace("D", "")) * -1)
                else:
                    conteudo[chave] = texto.replace("C", "")
            elif "numero_corretora" in chave:
                conteudo[chave] = str(texto.rsplit()[0])
            else:
                conteudo[chave] = str(texto)
    return conteudo


def inserir_banco_de_dados(nota, operacao, tipo_nota):
    db_n = tipo[tipo_nota]["nota_db"]
    db_c = tipo[tipo_nota]["operacao_db"]

    nota_db = db_n.query.filter_by(nr_nota=nota['nr_nota']).first()
    if not nota_db:
        nota_db = db_n(**nota)
        db.session.add(nota_db)

    for operação in operacao.values():
        operação_db = db_c.query.filter_by(**operação).first()
        if not operação_db:
            operação_db = db_c(nota_id=nota_db.id, **operação)
            db.session.add(operação_db)

    db.session.commit()

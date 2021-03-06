from pdfminer.high_level import extract_pages
from pdfminer.layout import LAParams, LTTextBoxHorizontal

from .extensions import db
from .models.bmf import FolhaBmf, NotaBmf, OperacaoBmf
from .models.bovespa import FolhaBovespa, NotaBovespa, OperacaoBovespa

cabecalho_bmf = {
    "numero_corretora": (480, 520, 90, 110),
    "nr_nota": (450, 490, 50, 70),
    "data_pregao": (520, 570, 50, 70),
    "cnpj_cpf": (460, 550, 130, 150),
    "codigo_cliente": (460, 550, 150, 170),
}

folha_bmf = {
    "folha": (490, 520, 50, 70),
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
    "cv": (30, 50, 182, 600),
    "mercadoria": (45, 90, 182, 600),
    "vencimento": (110, 160, 182, 600),
    "quantidade": (200, 230, 182, 600),
    "preco_ajuste": (230, 285, 182, 600),
    "tipo_negocio": (285, 370, 182, 600),
    "valor_operacao": (380, 460, 182, 600),
    "dc": (460, 480, 182, 600),
    "taxa_operacional": (540, 570, 182, 600),
    "preco_medio_compra": (0, 0, 0, 0),
    "preco_medio_venda": (0, 0, 0, 0),
}

cabecalho_b3 = {
    "numero_corretora": (440, 500, 160, 180),
    "nr_nota": (435, 470, 50, 70),
    "data_precao": (520, 570, 50, 70),
    "cnpj_cpf": (420, 480, 140, 160),
    "codigo_cliente": (35, 70, 140, 160),
}

folha_b3 = {
    "folha": (490, 520, 50, 70),
    "debentures": (200, 300, 455, 475),
    "vendas_vista": (200, 300, 465, 485),
    "compras_vista": (200, 300, 475, 495),
    "compra_opcoes": (200, 300, 485, 505),
    "venda_opcoes": (200, 300, 495, 510),
    "operacoes_termo": (200, 300, 505, 520),
    "valor_operacoes_titulos_publ": (200, 300, 515, 525),
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

operacao_b3 = {
    "q": (30, 45, 250, 450),
    "negociacao": (40, 80, 250, 450),
    "cv": (90, 110, 250, 450),
    "tipo_mercado": (105, 160, 250, 450),
    "prazo": (170, 188, 250, 450),
    "especifica????o_titulo": (185, 300, 250, 450),
    "obs": (300, 340, 250, 450),
    "quantidade": (330, 390, 250, 450),
    "preco_ajuste": (390, 450, 250, 450),
    "valor_operacao": (450, 550, 250, 450),
    "dc": (545, 560, 250, 450),
    "preco_medio_compra": (0, 0, 0, 0),
    "preco_medio_venda": (0, 0, 0, 0),
}


def principal(arquivo_pdf):
    laparams = LAParams(
        char_margin=0.5,
        line_margin=0.0,
    )
    for layout in extract_pages(arquivo_pdf, laparams=laparams):
        objetos: list = []
        tamanho_eixo_y = layout.y1
        objetos = [obj for obj in layout._objs if isinstance(obj, LTTextBoxHorizontal)]

        tipo_da_nota = verificar_tipo_da_nota(objetos)
        dicionario_bbox_texto = criar_dicionario_bbox_texto(objetos, tamanho_eixo_y)
        if "BM&F" in tipo_da_nota:
            banco_nota = NotaBmf
            banco_folha = FolhaBmf
            banco_operacao = OperacaoBmf
            cabe??alho = seleciona_textos_nota(dicionario_bbox_texto, cabecalho_bmf)
            folha = seleciona_textos_nota(dicionario_bbox_texto, folha_bmf)
            operacao = seleciona_textos_nota(dicionario_bbox_texto, operacao_bmf)

        elif "BOVESPA" in tipo_da_nota:
            banco_nota = NotaBovespa
            banco_folha = FolhaBovespa
            banco_operacao = OperacaoBovespa
            cabe??alho = seleciona_textos_nota(dicionario_bbox_texto, cabecalho_b3)
            folha = seleciona_textos_nota(dicionario_bbox_texto, folha_b3)
            operacao = seleciona_textos_nota(dicionario_bbox_texto, operacao_b3)
        else:
            break

        tratar_texto(cabe??alho)
        tratar_texto(folha)
        tratar_texto(operacao)
        preco_bmf_day_trade(operacao)
        inserir_banco_de_dados(
            cabe??alho,
            banco_nota,
            folha,
            banco_folha,
            operacao,
            banco_operacao,
        )


def verificar_tipo_da_nota(objetos):
    tipo_de_nota = ""
    for obj in objetos:
        if "BM&F" in obj.get_text():
            tipo_de_nota = "BM&F"
            break
        elif "BOVESPA" in obj.get_text():
            tipo_de_nota = "BOVESPA"
            break
    return tipo_de_nota


def criar_dicionario_bbox_texto(objetos, tamanho_eixo_y):
    bbox = {}
    for obj in objetos:
        x0, y1, x1, y0 = obj.bbox
        bbox[
            int(x0),
            int(x1),
            int(tamanho_eixo_y - y0),
            int(tamanho_eixo_y - y1),
        ] = obj.get_text().strip()
    return bbox


def seleciona_textos_nota(dicionario_bbox_texto, posi????es):
    textos_da_nota = dict()
    for bbox, texto in dicionario_bbox_texto.items():
        for campo, bboxmodelo in posi????es.items():
            if (
                bbox[0] >= bboxmodelo[0]
                and bbox[1] <= bboxmodelo[1]
                and bbox[2] >= bboxmodelo[2]
                and bbox[3] <= bboxmodelo[3]
            ):
                if "cv" in posi????es:
                    linha = bbox[3]
                    if linha in textos_da_nota:
                        textos_da_nota[linha][campo] = texto
                    else:
                        textos_da_nota[linha] = dict()
                        textos_da_nota[linha][campo] = texto
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
                .replace("@", "")
                .replace("    ", "")
                .replace("-", "")
                .strip()
            )
            if chave == "irrf_day_trade":
                conteudo[chave] = texto.split(" ")[5]
            elif chave == "irrf_proje????o":
                conteudo[chave] = texto.split(" ")[-1]
            elif "folha" in conteudo:
                if "D" in texto or "C" in texto:
                    if "D" in texto:
                        conteudo[chave] = str(float(texto.replace("D", "")) * -1)
                    else:
                        conteudo[chave] = texto.replace("C", "")
            elif "n??mero_corretora" in chave:
                conteudo[chave] = str(texto.rsplit()[0])
            else:
                conteudo[chave] = str(texto)
    return conteudo


def preco_bmf_day_trade(operacoes):

    for chave, operacao in operacoes.items():
        valor = float(operacao["preco_ajuste"])
        if "DAY TRADE" in operacao.get("tipo_negocio"):
            if operacao.get("cv") == "C":
                custo = valor * 0.0019
                operacoes[chave]["preco_medio_compra"] = valor + custo
            elif operacao.get("cv") == "V":
                custo = valor * 0.019
                operacoes[chave]["preco_medio_venda"] = valor + custo

        else:
            if operacao.get("cv") == "C":
                custo = valor * 0.005
                operacoes[chave]["preco_medio_compra"] = valor + custo

            elif operacao.get("cv") == "V":
                custo = valor * 0.018
                operacoes[chave]["preco_medio_venda"] = valor + custo


def inserir_banco_de_dados(
    cabecalho,
    banco_nota,
    folha,
    banco_folha,
    operacao,
    banco_operacao,
):

    nota_db = banco_nota.query.filter_by(**cabecalho).first()
    if not nota_db:
        nota_db = banco_nota(**cabecalho)
        db.session.add(nota_db)

    folha_db = banco_folha.query.filter_by(nota_id=nota_db.id, **folha).first()
    if not folha_db:
        folha_db = banco_folha(nota_id=nota_db.id, **folha)
        db.session.add(folha_db)

    for opera????o in operacao.values():
        opera????o_db = banco_operacao.query.filter_by(
            folha_id=folha_db.id, **opera????o
        ).first()
        if not opera????o_db:
            opera????o_db = banco_operacao(folha_id=folha_db.id, **opera????o)
            db.session.add(opera????o_db)

    db.session.commit()

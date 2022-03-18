from pdfminer.high_level import extract_pages
from pdfminer.layout import LAParams, LTTextBoxHorizontal

from .extensions import db
from .models.bmf import Folhasbmf, Operaçõesbmf, Notasbmf
from .models.bovespa import Folhasbovespa, Operaçõesbovespa, Notasbovespa

cabeçalho_bmf = {
    "número_corretora": (480, 520, 90, 110),
    "nr_nota": (450, 490, 50, 70),
    "data_pregão": (520, 570, 50, 70),
    "cnpj_cpf": (460, 550, 130, 150),
    "código_cliente": (460, 550, 150, 170),
}

folha_bmf = {
    "folha": (490, 520, 50, 70),
    "venda_disponível": (110, 140, 630, 655),
    "compra_disponível": (200, 250, 630, 655),
    "venda_opções": (330, 360, 630, 655),
    "compra_opções": (430, 470, 630, 655),
    "valor_negócios": (510, 590, 630, 655),
    "irrf": (110, 140, 650, 675),
    "irrf_day_trade_proj": (220, 250, 650, 675),
    "taxa_operacional": (280, 360, 650, 675),
    "taxas_bmf": (500, 570, 650, 675),
    "taxa_registro_bmf": (400, 480, 650, 675),
    "outros_custos": (170, 190, 675, 700),
    "impostos": (210, 250, 675, 700),
    "ajuste_posição": (280, 350, 675, 700),
    "ajuste_day_trade": (390, 460, 675, 700),
    "total_despesas": (540, 570, 675, 700),
    "outros": (50, 90, 700, 720),
    "irrf_operacional": (110, 150, 700, 720),
    "total_conta_investimento": (200, 250, 700, 720),
    "total_conta_normal": (310, 350, 700, 720),
    "total_líquido": (420, 460, 700, 720),
    "total_líquido_nota": (500, 600, 700, 720),
}

operações_bmf = {
    "cv": (30, 50, 182, 600),
    "mercadoria": (45, 90, 182, 600),
    "vencimento": (110, 160, 182, 600),
    "quantidade": (200, 230, 182, 600),
    "preço_ajuste": (230, 285, 182, 600),
    "tipo_negócio": (285, 370, 182, 600),
    "valor_operação": (380, 460, 182, 600),
    "dc": (460, 480, 182, 600),
    "taxa_operacional": (540, 570, 182, 600),
}

cabeçalho_b3 = {
    "número_corretora": (440, 500, 160, 180),
    "nr_nota": (435, 470, 50, 70),
    "folha": (490, 520, 50, 70),
    "data_pregão": (520, 570, 50, 70),
    "cnpj_cpf": (420, 480, 140, 160),
    "código_cliente": (35, 70, 140, 160),
}

folha_b3 = {
    "debêntures": (200, 300, 455, 475),
    "vendas_vista": (200, 300, 465, 485),
    "compras_vista": (200, 300, 475, 495),
    "compra_opções": (200, 300, 485, 505),
    "venda_opções": (200, 300, 495, 510),
    "operações_termo": (200, 300, 505, 520),
    "valor_operações_títulos_públ": (200, 300, 515, 525),
    "valor_operações": (200, 300, 525, 545),
    "valor_líquido_operações": (450, 560, 465, 480),
    "taxa_liquidação": (450, 560, 475, 490),
    "taxa_registro": (450, 560, 485, 500),
    "total_clbc": (450, 560, 495, 506),
    "taxa_termo_opções": (450, 560, 510, 525),
    "taxa_ana": (450, 560, 525, 535),
    "emolumentos": (450, 560, 530, 545),
    "total_bovespa": (450, 560, 540, 555),
    "taxa_operacional": (450, 560, 565, 580),
    "execução": (450, 560, 575, 590),
    "taxa_custódia": (450, 560, 585, 600),
    "impostos": (450, 560, 595, 610),
    "irrf": (450, 560, 605, 620),
    "outros": (450, 560, 615, 630),
    "total_custos_despesas": (450, 560, 625, 640),
    "líquido": (450, 560, 635, 655),
}

operações_b3 = {
    "q": (30, 45, 250, 450),
    "negociação": (40, 80, 250, 450),
    "cv": (90, 110, 250, 450),
    "tipo_mercado": (105, 160, 250, 450),
    "prazo": (170, 190, 250, 450),
    "especificação_título": (190, 300, 250, 450),
    "obs": (300, 340, 250, 450),
    "quantidade": (330, 390, 250, 450),
    "preço_ajuste": (390, 450, 250, 450),
    "valor_operação": (450, 550, 250, 450),
    "dc": (545, 560, 250, 450),
}


def principal(arquivo_pdf: str) -> None:
    laparams = LAParams(
        char_margin=0.5,
        line_margin=0.0,
    )
    for layout in extract_pages(arquivo_pdf, laparams=laparams):
        objetos: list = []
        tamanho_eixo_y = layout.y1
        for obj in layout._objs:
            if isinstance(obj, LTTextBoxHorizontal):
                objetos.append(obj)
            else:
                break

        tipo_da_nota = verificar_tipo_da_nota(objetos)
        dicionario_bbox_texto = criar_dicionario_bbox_texto(
            objetos, tamanho_eixo_y
        )
        if "BM&F" in tipo_da_nota:
            banco_notas = Notasbmf
            banco_folhas = Folhasbmf
            banco_operações = Operaçõesbmf
            cabeçalho = seleciona_textos_nota(
                dicionario_bbox_texto, cabeçalho_bmf
            )
            folha = seleciona_textos_nota(dicionario_bbox_texto, folha_bmf)
            operações = seleciona_textos_nota(
                dicionario_bbox_texto, operações_bmf
            )

        elif "BOVESPA" in tipo_da_nota:
            banco_notas = Notasbovespa
            banco_folhas = Folhasbovespa
            banco_operações = Operaçõesbovespa
            cabeçalho = seleciona_textos_nota(
                dicionario_bbox_texto, cabeçalho_b3
            )
            folha = seleciona_textos_nota(dicionario_bbox_texto, folha_b3)
            operações = seleciona_textos_nota(
                dicionario_bbox_texto, operações_b3
            )
        else:
            break

        tratar_texto(cabeçalho)
        tratar_texto(folha)
        tratar_texto(operações)
        inserir_banco_de_dados(
            cabeçalho,
            banco_notas,
            folha,
            banco_folhas,
            operações,
            banco_operações,
        )


def verificar_tipo_da_nota(objetos: list) -> str:
    tipo_de_nota = ""
    for obj in objetos:
        if "BM&F" in obj.get_text():
            tipo_de_nota = "BM&F"
            break
        elif "BOVESPA" in obj.get_text():
            tipo_de_nota = "BOVESPA"
            break
    return tipo_de_nota


def criar_dicionario_bbox_texto(objetos: list, tamanho_eixo_y: int) -> dict:
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


def seleciona_textos_nota(dicionario_bbox_texto: dict, posições: dict) -> dict:
    textos_da_nota: dict = dict()
    for bbox, texto in dicionario_bbox_texto.items():
        for campo, bboxmodelo in posições.items():
            if (
                bbox[0] >= bboxmodelo[0]
                and bbox[1] <= bboxmodelo[1]
                and bbox[2] >= bboxmodelo[2]
                and bbox[3] <= bboxmodelo[3]
            ):
                if "cv" in posições:
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


def tratar_texto(conteudo: dict) -> dict:
    for chave, texto in conteudo.items():
        if isinstance(texto, dict):
            tratar_texto(texto)
        else:
            texto = (
                texto.replace("|", "")
                .replace(".", "")
                .replace(",", ".")
                .replace("@", "")
                .strip()
            )
            if " D" in texto or " C" in texto:
                if "D" in texto:
                    conteudo[chave] = str(float(texto.replace("D", "")) * -1)
                else:
                    conteudo[chave] = texto.replace("C", "")
            elif "numero_da_corretora" in chave:
                conteudo[chave] = str(texto.rsplit()[0])
            else:
                conteudo[chave] = str(texto)
    return conteudo


def inserir_banco_de_dados(
    cabeçalho: dict,
    banco_notas: db,
    folhas: dict,
    banco_folhas: db,
    operações: dict,
    banco_operações: db,
) -> None:

    nota_db = banco_notas.query.filter_by(**cabeçalho).first()

    if not nota_db:
        nota_db = banco_notas(**cabeçalho)

    folha = banco_folhas.query.filter_by(notasbmf_id=nota_db.id, **folhas).first()

    if not folha:
        folha = banco_folhas(notasbmf=nota_db, **folhas)

    for operação in operações.values():
        operação_db = banco_operações.query.filter_by(folhasbmf_id=folha.id, **operação).first()
        if not operação_db:
            operação_db = banco_operações(folhasbmf=folha, **operação)

        db.session.add(operação_db)
    db.session.commit()

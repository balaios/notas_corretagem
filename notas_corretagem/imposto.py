def calcular_imposto(nota):
    notas = nota.query.all()
    papéis = {}

    for nota in notas:
        data = nota.data_pregão
        for folhas in nota.folhas_bovespa:
            for operação in folhas.operações_bovespa:
                papel = operação.especificação_título
                quantidade = int(operação.quantidade)
                preço = float(operação.valor_operação)
                tipo = operação.cv

                if papéis.get(data):
                    if papéis[data].get(papel):
                        papéis[data][papel]["quantidade"] += quantidade
                        papéis[data][papel]["preço"] += preço
                    else:
                        papéis[data][papel] = dict()
                        papéis[data][papel]["quantidade"] = quantidade
                        papéis[data][papel]["preço"] = preço
                        papéis[data][papel]["tipo"] = tipo
                else:
                    papéis[data] = dict()
                    papéis[data][papel] = dict()
                    papéis[data][papel]["quantidade"] = quantidade
                    papéis[data][papel]["preço"] = preço
                    papéis[data][papel]["tipo"] = tipo

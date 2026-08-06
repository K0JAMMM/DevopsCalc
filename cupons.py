def obter_desconto_do_cupom(cupom):
    if cupom is None:
        return 0

    cupons = {
        "DEVOPS10": 10,
    }

    cupom = cupom.upper()

    if cupom not in cupons:
        raise ValueError("Cupom inválido.")

    return cupons[cupom]
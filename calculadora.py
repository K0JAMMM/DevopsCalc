from cupons import obter_desconto_do_cupom


def calcular_total(itens, desconto_percentual=0, cupom=None):
    if not 0 <= desconto_percentual <= 100:
        raise ValueError("O desconto precisa estar entre 0 e 100.")

    subtotal = sum(
        preco_unitario * (1 - desconto_item / 100) * quantidade
        for preco_unitario, desconto_item, quantidade in itens
    )

    desconto_total = desconto_percentual + obter_desconto_do_cupom(cupom)
    desconto_total = min(desconto_total, 100)

    total = subtotal * (1 - desconto_total / 100)

    return round(total, 2)
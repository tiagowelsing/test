def analisar_lista(lista):

    if not lista:  # Verifica se a lista está vazia
        return "A lista está vazia"
    
    soma = sum(lista)
    max_num = max(lista)
    min_num = min(lista)
    media = soma / len(lista)
    
    return {
        "soma": soma,
        "max": max_num,
        "min": min_num,
        "media": media
    }

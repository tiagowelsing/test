def analisar_lista(lista):

    if not lista:  # Verifica se a lista está vazia
        return "A lista está vazia"
    
    quantidade_pares = len([num for num in lista if num % 2 == 0])
    
    max_num = max(lista)
    min_num = min(lista)
    media = sum(lista) / len(lista)
    
    return {
        "quantidade_pares": quantidade_pares,
        "max": max_num,
        "min": min_num,
        "media": media
    }

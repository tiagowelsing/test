from funcao import analisar_lista

numeros = [10, 5, 20, 15, 30]

resultado = analisar_lista(numeros)

print("Resultados da análise:")
print(f"Soma: {resultado['soma']}")
print(f"Máximo: {resultado['max']}")
print(f"Mínimo: {resultado['min']}")
print(f"Média: {resultado['media']}")

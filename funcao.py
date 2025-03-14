custos = [350, 850, 400, 630] 
ganhos = [2800, 200, 1800]      

def somatorio(lista):
    total = 0
    contador = 0
    while contador <len(lista):
        total = total + lista(contador)
        contador = contador + 1 
        return total
total_custos = somatorio(custos)
total_ganhos = somatorio(ganhos)

diferenca = total_ganhos - total_custos

print(f"total de Custos: R$(total_custos)")
print(f"tota de Ganhos: R$(total_ganhos)")
print(f"Diferença (ganhos - custos): R$(diferenca)")


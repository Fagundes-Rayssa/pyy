custos = [900, 350, 300, 400] 
ganhos = [2500, 500, 1200]      

def somatorio(lista):
    return sum(lista)

d = somatorio(ganhos) - somatorio(custos)

print(f"Custos: R${sum(custos)}")
print(f"Ganhos: R${sum(ganhos)}")
print(f"Diferença: R${d}")


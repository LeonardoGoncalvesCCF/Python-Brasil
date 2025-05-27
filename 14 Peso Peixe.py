print("-----------------------------------------------------")

peso_peixe = float(input(" Qual o peso do peixe: "))
limite_peso_peixe = 50
excesso = peso_peixe - limite_peso_peixe
multa = excesso * 4
excedeu = peso_peixe > limite_peso_peixe

print("-|                                                               |-")

if excedeu:
    print(f" O Peso do peixe é {peso_peixe}. O limite é de {limite_peso_peixe}")
    print(f" O peixe pesa {excesso}Kg a mais do que o permitido")
    print(f" Como o peso foi excedido a multa é de R${multa} ")

elif peso_peixe == limite_peso_peixe:
    print(f" O Peso do peixe é {peso_peixe}Kg e esta dentro do limite de {limite_peso_peixe}Kg")

elif peso_peixe < limite_peso_peixe:
    print(" O peso do peixe esta dentro do limite ")

print("-----------------------------------------------------")

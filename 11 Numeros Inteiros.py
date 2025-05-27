print("-----------------------------------------------------")
print(" Digite dois numero inteiros e um numero real!! ")
numero_inteiro = int(input(" Digite um número inteiro: "))
numero_inteiro2 = int(input(" Digite outro número inteiro: "))
numero_real = float(input(" Digite um número real: "))
print("-----------------------------------------------------")

produto = (numero_inteiro * 2) * (numero_inteiro2 / 2 )

soma = (numero_inteiro * 3) + numero_real

elevado = numero_real ** 3

print(" O Resultado das operações são: ")

print(f" O produto do dobro do primeiro com metade do segundo é: {produto}")
print(f" A soma do triplo do primeiro com o terceiro é: {soma}")
print(f" O terceiro elevado a cubo é: {elevado}")

print("-----------------------------------------------------")

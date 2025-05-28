print("-----------------------------------------------------")

parede = float(input(" Quantos metros quadrados serão pintados: "))

# Lata tem 18 litros
# 1 litro = 3 metros quadrados
# 1 lata = 18 litros = 54 metros quadrados

#
lata_de_tinta_litros = 18 
preco_lata_de_tinta = 80
metro_quadrado_lata = 54
cobertura_lata_litro = 3

quantidade_de_litros = parede / cobertura_lata_litro

# 

eh_maior_ou_nao_lata = quantidade_de_litros >= lata_de_tinta_litros

# Calculando a quantidade de latas necessárias


print("-----------------------------------------------------")

if not eh_maior_ou_nao_lata:
    print(f" Você quer pintar {parede} metros quadrados ")
    print(" Uma lata de tinta tem 18 litros, isso cobre uma area de 54 metros quadrados ")
    print(f" Você precisará de 1 e custará R${preco_lata_de_tinta} ")
    
else :
    quantidade_de_litros_finais = quantidade_de_litros / lata_de_tinta_litros

    eh_float = isinstance(quantidade_de_litros_finais, float)
    if eh_float:
        quantidade_de_latas_int = int(quantidade_de_litros_finais + 1)

    print(f" A quantidade de latas necessárias é {quantidade_de_latas_int} e o valor é {preco_lata_de_tinta * quantidade_de_latas_int} ")


print("-----------------------------------------------------")


print("-----------------------------------------------------")


parede = float(input(" Quantos metros quadrados serão pintados: "))

# ------------- LATA DE TINTA 1 --------------#
# Lata 1 tem 18 litros                        #
# 1 litro = 6 metros quadrados                #
# 1 lata = 18 litros = 54 metros quadrados    #
# Valor = 80                                  #
# --------------------------------------------#

# ------------- LATA DE TINTA 2 --------------#
# Lata 2 tem 3,6 litros                       #
# 1 litro = 6 metros quadrados                #
# 1 lata = 3,6 litros = 21,6 metros quadrados #
# Valor = 25                                  #
# --------------------------------------------#

# Lata de tinta 1
lata_de_tinta_1 = 18 
preço_lata_de_tinta_1 = 80
metro_quadrado_lata_1 = 54

# Lata de tinta 2
lata_de_tinta_2 = 3.6 
preço_lata_de_tinta_2 = 25
metro_quadrado_lata_2 = 21.6 

# Calculando lata de 18 litros
quantas_latas_1 = parede / metro_quadrado_lata_1

if quantas_latas_1 == int(quantas_latas_1):
    print(f" Serão necessárias {int(quantas_latas_1)} latas de 18 litros.")

# Calculando lata de 3.6 litros
quantas_latas_2 = parede / metro_quadrado_lata_2

if quantas_latas_2:
    print(f" Serão necessárias {quantas_latas_2} latas de 18 litros.   TESTE TESTE")

if parede >= metro_quadrado_lata_2:
    quantas_latas_2 = parede / metro_quadrado_lata_2
    print(f"Você precisa de {quantas_latas_2} latas de 3,6 litros ")





print("-----------------------------------------------------")

#if parede > metro_quadrado_lata_1 and parede > metro_quadrado_lata_2:
#    print(f" Você quer pintar {parede} metros quadrados ")
#    print(f" Comprando apenas galoes de 18 litros você precisará de {quantas_latas_1} ")
#    print(f" Comprando apenas galoes de 3,6 litros você precisará de {quantas_latas_2} ")


# print("-----------------------------------------------------")

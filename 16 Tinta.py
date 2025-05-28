print("-----------------------------------------------------")

parede = float(input(" Quantos metros quadrados serão pintados: "))

# Lata tem 18 litros
# 1 litro = 3 metros quadrados
# 1 lata = 18 litros = 54 metros quadrados


lata_de_tinta = 18 
preço_lata_de_tinta = 80
metro_quadrado_lata = 54

print("-----------------------------------------------------")

if parede > metro_quadrado_lata:
    print(f" Voce quer pintar {parede} metros quadrados ")
    print(" Uma lata de tinta tem 18 litros, isso cobre uma area de 54 metros quadrados ")
    print(" Você precisará de mais de uma lata de tinta para pintar a parede ")
else :
    print(f" Voce quer pintar {parede} metros quadrados ")
    print(" Voce precisa de apenas uma Lata de Tinta")


print("-----------------------------------------------------")


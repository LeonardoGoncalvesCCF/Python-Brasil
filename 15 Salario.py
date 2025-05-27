print("-----------------------------------------------------")

horas_trabalhadas = float(input(" Quantas horas você trabalhou: "))
dinheiro_por_hora = float(input(" Digite quanto você ganha por hora: "))

# Descontos
INSS = 0.11 # 11%
IR = 0.08   # 8%
Sindicato = 0.05 # 5%

# Calculando o salário bruto
horas_mes = horas_trabalhadas * 30
salario_bruto = horas_mes * dinheiro_por_hora

# Caculando os desncontos
desconto_inss = salario_bruto * INSS
desconto_ir = salario_bruto * IR
desconto_sindicato = salario_bruto * Sindicato

# Salario Líquido
salario_liquido = salario_bruto - (desconto_inss + desconto_ir + desconto_sindicato)

print("-----------------------------------------------------")
print(f" Salario Bruto: {salario_bruto:.2f} ")
print(f" Salario Liquido: {salario_liquido:.2f} ")
print(f" Descontos INNS: {INSS}, IR: {IR}, Sindicato: {Sindicato} ")
print("-----------------------------------------------------")


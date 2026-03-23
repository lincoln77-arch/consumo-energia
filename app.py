# Entrada de dados
btus = 12000
horas = 8
dias = 30
tarifa = 0.90

# Potência base (W)
potencia_base = btus * 0.293

# Consumo Inverter (≈ 50%)
pot_inverter = potencia_base * 0.5
consumo_inverter = (pot_inverter * horas * dias) / 1000
custo_inverter = consumo_inverter * tarifa

# Consumo Convencional (100%)
pot_convencional = potencia_base
consumo_convencional = (pot_convencional * horas * dias) / 1000
custo_convencional = consumo_convencional * tarifa

# Classificação simples de consumo
if consumo_inverter < 200:
    nivel = "Baixo"
elif consumo_inverter < 500:
    nivel = "Médio"
else:
    nivel = "Alto"

# Economia
economia_reais = custo_convencional - custo_inverter
economia_percentual = (economia_reais / custo_convencional) * 100

# Texto base + saída
print("=== Análise de Consumo ===")
print(f"Consumo mensal (Inverter): {consumo_inverter:.2f} kWh")
print(f"Custo mensal (Inverter): R$ {custo_inverter:.2f}")
print(f"Nível de consumo: {nivel}")

print("\n=== Comparativo ===")
print(f"Convencional: {consumo_convencional:.2f} kWh | R$ {custo_convencional:.2f}")
print(f"Inverter: {consumo_inverter:.2f} kWh | R$ {custo_inverter:.2f}")

print("\n=== Economia ===")
print(f"Economia: R$ {economia_reais:.2f}")
print(f"Redução: {economia_percentual:.2f}%")

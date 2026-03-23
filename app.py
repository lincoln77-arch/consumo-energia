# Calculadora de Consumo - Ar Condicionado ❄️

print("=== Calculadora de Consumo de Energia ===\n")

btus = int(input("Informe a capacidade (BTUs): "))
horas = float(input("Horas de uso por dia: "))
tipo = input("Tipo (convencional/inverter): ").lower()

potencia_base = btus * 0.293

potencia_conv = potencia_base
potencia_inv = potencia_base * 0.5

if tipo == "inverter":
    potencia = potencia_inv
else:
    potencia = potencia_conv

consumo = (potencia * horas * 30) / 1000

consumo_conv = (potencia_conv * horas * 30) / 1000
consumo_inv = (potencia_inv * horas * 30) / 1000

tarifa = 0.90

custo = consumo * tarifa
custo_conv = consumo_conv * tarifa
custo_inv = consumo_inv * tarifa

def nivel(valor):
    if valor < 150:
        return "Baixo"
    elif valor < 400:
        return "Médio"
    else:
        return "Alto"

print("\n--- Resultado ---")
print(f"Capacidade: {btus} BTUs")
print(f"Tipo: {tipo}")
print(f"Consumo: {consumo:.2f} kWh/mês")
print(f"Custo: R$ {custo:.2f}")
print(f"Nível de consumo: {nivel(consumo)}")

print("\n--- Comparativo ---")
print(f"Convencional: {consumo_conv:.2f} kWh | R$ {custo_conv:.2f}")
print(f"Inverter: {consumo_inv:.2f} kWh | R$ {custo_inv:.2f}")

economia = custo_conv - custo_inv
print(f"Economia com inverter: R$ {economia:.2f}/mês")

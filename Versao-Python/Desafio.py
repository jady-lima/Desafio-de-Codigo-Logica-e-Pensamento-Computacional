def calcular_imposto(valor_salario):
    if (valor_salario >= 0 and valor_salario <= 1100):
        imposto = 0.05
    elif (valor_salario > 1100 and valor_salario <= 2500):
        imposto = 0.10
    else:
        imposto = 0.15
    return imposto * valor_salario

valor_salario = float(input())
valor_beneficios = float(input())

valor_imposto = calcular_imposto(valor_salario)

saida = valor_salario - valor_imposto + valor_beneficios
print(f"{saida:.2f}")
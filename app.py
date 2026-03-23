def calcular_consumo(potencia, horas_dia):
    return (potencia * horas_dia * 30) / 1000


def calcular_custo(consumo, tarifa=0.75):
    return consumo * tarifa


def calcular_aparelho():
    print("\n Novo cálculo de consumo\n")

    aparelho = input("Nome do aparelho: ")

    try:
        potencia = float(input("Potência (W): "))
        horas_dia = float(input("Horas por dia: "))
    except ValueError:
        print("Entrada inválida. Use apenas números.")
        return

    consumo = calcular_consumo(potencia, horas_dia)
    custo = calcular_custo(consumo)

    print("\n Resultado:")
    print(f"Aparelho: {aparelho}")
    print(f"Consumo: {consumo:.2f} kWh/mês")
    print(f"Custo: R$ {custo:.2f}/mês")


def mostrar_menu():
    print("\n" + "=" * 30)
    print("CALCULADORA DE ENERGIA")
    print("=" * 30)
    print("1 - Calcular consumo de aparelho")
    print("2 - Sobre o sistema")
    print("3 - Sair")


def sobre():
    print("\n Sobre o sistema")
    print("Este programa calcula o consumo mensal de energia")
    print("com base na potência e tempo de uso diário.")
    print("Ideal para estimativas simples de gastos.")


def main():
    while True:
        mostrar_menu()
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            calcular_aparelho()

        elif opcao == "2":
            sobre()

        elif opcao == "3":
            print("\n Encerrando o programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
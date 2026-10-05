def celsius_para_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def celsius_para_kelvin(celsius):
    return celsius + 273.15


def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def fahrenheit_para_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 + 273.15


def kelvin_para_celsius(kelvin):
    return kelvin - 273.15


def kelvin_para_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9 / 5 + 32


while True:

    print("\n===== CONVERSOR DE TEMPERATURAS =====")
    print("1 - Celsius para Fahrenheit")
    print("2 - Celsius para Kelvin")
    print("3 - Fahrenheit para Celsius")
    print("4 - Fahrenheit para Kelvin")
    print("5 - Kelvin para Celsius")
    print("6 - Kelvin para Fahrenheit")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Programa encerrado!")
        break

    if opcao not in ["1", "2", "3", "4", "5", "6"]:
        print("Opção inválida!")
        continue

    temperatura = float(input("Digite a temperatura: "))

    if opcao == "1":
        resultado = celsius_para_fahrenheit(temperatura)
        print(f"Resultado: {resultado:.2f} °F")

    elif opcao == "2":
        resultado = celsius_para_kelvin(temperatura)
        print(f"Resultado: {resultado:.2f} K")

    elif opcao == "3":
        resultado = fahrenheit_para_celsius(temperatura)
        print(f"Resultado: {resultado:.2f} °C")

    elif opcao == "4":
        resultado = fahrenheit_para_kelvin(temperatura)
        print(f"Resultado: {resultado:.2f} K")

    elif opcao == "5":
        resultado = kelvin_para_celsius(temperatura)
        print(f"Resultado: {resultado:.2f} °C")

    elif opcao == "6":
        resultado = kelvin_para_fahrenheit(temperatura)
        print(f"Resultado: {resultado:.2f} °F")

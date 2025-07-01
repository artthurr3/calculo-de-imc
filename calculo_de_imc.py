nome = input("Qual é o nome do paciente? ")
peso = float(input(f"Qual é o peso do paciente {nome}? "))
altura = float(input(f"Qual é a altura do paciente {nome}? "))

IMC = peso / (altura * altura)

if IMC <= 18.5:
    print("Está abaixo do peso")
elif IMC <=24.9:
    print("Peso normal")
elif IMC <= 29.9:
    print("Sobrepeso")
elif IMC <= 34.9:
    print("Obesidade grau I")
elif IMC <= 39.9:
    print("Obesidade grau II")
else:
    print("Para de comer xtudo fi😡")
print("-"*20,"Peso ideal","-"*20,"\n\t")
while True:
  sexo = input("Qual seu gênero? (Digite M para Mulher e H para Homem): ")
  altura = input("Digite a sua altura em metros: ")

  if altura == '':
    print(f"Altura inválida. Tente novamente.")
    continue

  altura_certa = float(altura)

  if sexo == 'M':
    peso_ideal = (62.1 * altura_certa) - 44.7
    print(f"O seu peso ideal é de {peso_ideal:.2f} kg.")
    break
  elif sexo == 'H':
    peso_ideal = (72.7 * altura_certa) - 58
    print(f"O seu peso ideal é de {peso_ideal} kg.")
    break
  else:
    print(f"Essa opção de gênero não existe. Tente novamente.")

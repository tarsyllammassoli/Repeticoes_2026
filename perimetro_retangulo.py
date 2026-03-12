import math
print("-"*20,"Altura e Base de um Retângulo","-"*20,"\n\t")
while True:
  h = float(input("Digite a Altura do Retângulo em Centímetros. (Deve ser > 0): "))
  if h < 0:
    print("A Altura deve ser maior que 0.")
    continue
  b = float(input("Digite a Base do Retângulo em Centímetros. (Deve ser > 0): "))
  if b < 0:
    print("A Base deve ser maior que 0.")
    continue
  
  centimetros = 2*b + 2*h
  polegadas = centimetros/2.54
  jardas = polegadas * 0.03

  print(f"Perímetro em\nCentímetros: {centimetros:.0f} \nPolegadas: {polegadas:.2f} \nJardas: {jardas:.4f}")
  break

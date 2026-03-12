import math
print("-"*20,"Volume e Área de Esfera","-"*20,"\n\t")
while True:
  r = float(input(f"Digite o valor do raio da esfera (Deve ser > 0 e Real): "))
  if r < 0:
    print(f"O número inserido é inválido. Tente novamente.")
    continue
  else:
    area = 4 * math.pi * (r**2)
    volume = (4/3) * math.pi * (r**3)
    print(f"A área é de {area:.2f} e o Volume é de {volume:.2f} .")
    break

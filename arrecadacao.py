print("-"*20,"Jogo de Futebol","-"*20,"\n\t")
ingresso = float(input("Digite o valor do ingresso: "))
ingresso_meia = ingresso / 2

print("Abaixo: Digite a quantidade exata das pessoas para obter o **Público Total**.\n(OBS: Abaixo de 18 paga meia entrada e acima de 18 apenas com 1KG de alimento não-perecível.)\n")

crianca = int(input(f"Crianças de até 10 anos: "))
jovem = int(input(f"\nJovens de 11 a 17: "))
adulto_com_alimento = int(input(f"\nAcima de 18 COM 1kg de alimento não perecível: "))
adulto_sem_alimento =  int(input(f"\nAcma de 18 SEM 1kg de alimento não perecível: "))

publico_total = crianca + jovem + adulto_com_alimento + adulto_sem_alimento
valor_total_inteira = ingresso * adulto_sem_alimento

if crianca and jovem and adulto_com_alimento:
  valor_total_meia = crianca * ingresso_meia + jovem * ingresso_meia + adulto_com_alimento * ingresso_meia

valor_total = valor_total_meia + valor_total_inteira

print(f"\nA arrecadação foi de R$ {valor_total}.")
print(f"\nO ingresso inteiro custou R$ {ingresso}.")
print(f"\nO ingresso meia custou R$ {ingresso_meia}.")
print(f"\nO público total foi de {publico_total}.")

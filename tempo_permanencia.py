print("-"*20,"Tempo em Sala","-"*20,"\n\t")
entrada = int(input("Que horas você entrou no Laboratório de Programação? (ex: 14): "))
durante = input("Você ainda está no Laboratório de Programação?\n(Digite S para SIM ou N para NÃO): ").upper()
if durante == 'N':
  saida = int(input("Quantos SEGUNDOS você ficou no Laboratório de Programação?:  "))
  if saida >= 0:
    horas = saida // 3600
    minutos = saida % 60
    segundos = saida % 3600
    segundos_finais = segundos // 60
    if horas > 0:
      print(f"Você permaneceu no Laboratório de Programação por {horas} horas, {minutos} minutos e {segundos_finais} segundos.")
    else:
      print(f"Você permaneceu no Laboratório de Programação por {minutos} minutos e {segundos_finais} segundos.")
elif durante == 'S':
  print(f"Que bom! Continue estudando bastante. Volte mais tarde para saber quanto tempo você ficou em sala.")

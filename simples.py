while True:
    answer = int(input(f"Digite a senha correta: "))
    if answer != 2608:
        print("Senha incorreta. Tente novamente.")
    else:
        print(f"Login feito com sucesso.")
        break

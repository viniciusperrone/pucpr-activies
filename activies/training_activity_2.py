options_text = ['1. Estudante', '2. Disciplina', '3. Professor', '4. Turma', '5. Matrícula', '6. Sair']

choose_option = 1

while choose_option != 6:
    print("\n------------Sistema PUC------------\n")

    for option in options_text:
        print(option)

    choose_option = int(input("\nDigite sua opção: "))

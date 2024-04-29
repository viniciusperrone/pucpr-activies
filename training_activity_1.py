continuos = True

options_text = ['1. Estudante', '2. Disciplina', '3. Professor', '4. Turma', '5. Matrícula']

print("------------Sistema PUC------------\n")

for option in options_text:
    print(option)

choose_option = int(input("\nDigite sua opção: "))

if choose_option < 1 or choose_option > 5:
    print("\nOpção inválida!")
else:
    print("\nFim do programa.")
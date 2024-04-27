MENU_MAIN_TEXT = """
Sistema PUC

1. Estudante
2. Disciplina
3. Professor
4. Turma
5. Matrícula

"""

MENU_MODULE_TEXT = """
Sistema PUC

1. Incluir
2. Listar
3. Excluir
4. Alterar

"""

def menu_main():
    print(MENU_MAIN_TEXT)

    choose_item = int(input("Digite sua opção: "))

    print("\n")

    return choose_item

def menu_item():
    print(MENU_MODULE_TEXT)

    choose_item = int(input("Digite sua opção: "))

    print("\n")

    return choose_item


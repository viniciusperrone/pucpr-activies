MENU_TEXT = """
Sistema PUC
        
1. Cadastrar Estudante
2. Cadastrar Disciplina
3. Cadastrar Professor
4. Cadatrar Turma
5. Cadastrar Matrícula

"""
def menu_main():
    print(MENU_TEXT)

    choose_item = int(input("Digite sua opção: "))

    print("\n")

    return choose_item


from subject import Subject
from typing import List

def created_subject(list_subject: List[Subject]) -> None:
    name_subject = input("Digite o nome: ")
    name_workload = input("Digite a carga horária: ")

    subject = Subject(name_subject, name_workload)

    list_subject.append(subject)

def list_subjects(list_subject: List[Subject]) -> None:
    print("Lista de Disciplinas.\n")
    for index, subject in enumerate(list_subject):
        print(f"[{index + 1}] - Disciplina")
        print(f"Nome: {subject.name}")
        print(f"Carga Horária: {subject.workload}\n")

def delete_subject(list_subject: List[Subject]) -> None:
    print("Lista de Disciplinas.\n")
    for index, subject in enumerate(list_subject):
        print(f"[{index + 1}] - {subject.name}\n")
    
    index_subject = int(input("Digite o número da disciplina que deseja excluir: "))

    subject = list_subject[index_subject - 1]

    if index_subject > len(list_subject) or index_subject < len(list_subject):
        print("Número de estudante errado ou estudante não existe!\n")

    list_subject.remove(subject)
    print("\nDisciplina removido.")


def update_subject(list_subject: List[Subject]) -> None:
    print("Lista de Disciplina.\n")
    for index, subject in enumerate(list_subject):
        print(f"[{index + 1}] - {subject.name}\n")

    index_subject = int(input("Digite o número da disciplina que deseja atualizar: "))

    subject = list_subject[index_subject - 1]

    if index_subject > len(list_subject) or index_subject < len(list_subject):
        print("Número de disciplina errado ou não existe!\n")

    name_subject = input("Digite o novo nome: ")
    workload_subject = input("Digite a nova carga horária: ")

    subject.name = name_subject
    subject.workload = workload_subject
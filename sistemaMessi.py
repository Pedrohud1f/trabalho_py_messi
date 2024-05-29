def adicionar_disciplina(disciplinas):
    titulo = input("Digite o título/nome da disciplina/curso: ")
    descricao = input("Digite a descrição: ")
    carga_horaria = input("Digite a carga horária: ")
    disciplina = {
        "Título": titulo, 
        "Descrição": descricao, 
        "Carga Horária": carga_horaria 
    }
    disciplinas.append(disciplina)
    print("Disciplina/curso adicionado com sucesso!")

def listar_disciplinas(disciplinas):
    if disciplinas:
        for i, disciplina in enumerate(disciplinas):
            print(f"{i+1}. Título: {disciplina['Título']}, Descrição: {disciplina['Descrição']}, Carga Horária: {disciplina['Carga Horária']}")
    else:
        print("Nenhuma disciplina/curso cadastrado.")

def main():
    disciplinas = []
    
    while True:
        print("\n----- Menu -----")
        print("1 - Adicionar Disciplina/Curso")
        print("2 - Listar Disciplinas/Cursos")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_disciplina(disciplinas)
        elif opcao == "2":
            listar_disciplinas(disciplinas)
        elif opcao == "3":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
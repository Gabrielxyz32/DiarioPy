from datetime import datetime
import json


def salvarEntradas():
    with open("diario.json", "w", encoding="utf-8") as arquivo:
        json.dump(entradas, arquivo, ensure_ascii=False, indent=4)

def carregarEntradas():
    try:
        with open("diario.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

entradas = carregarEntradas()

def excluirEntrada():
    exibeEntradas()
    
    while True:
        try:
            escolha = int(input("Escolha o índice de qual entrada excluir:"))
            break

        except:
            print("Escolha inválida")

    for indice, entrada in enumerate(entradas, start=1):
        if (escolha == indice):
            print(f"Você escolheu: {entrada['Titulo']}")
            entradas.pop(indice - 1)
            salvarEntradas()
            return

def menuDiario():
    print("Diário Pessoal no Python")
    print("1 - Inserir nota neste dia")
    print("2 - Exibir notas neste dia")
    print("3 - Exibir todas as notas")
    print("4 - Pesquisar entradas")
    print("5 - Excluir entradas")
    print("6 - Sair")

def addEntrada(titulo, texto):
    entrada = {
        "Titulo": titulo,
        "Texto": texto,
        "Data": datetime.now().strftime("%d/%m/%Y")
    }

    entradas.append(entrada)
    salvarEntradas()

def exibeEntradas():
    if (entradas == []) :
        print("Nenhuma entrada registrada")
        return


    for indice, entrada in enumerate(entradas, start=1) :
        print()
        print(f"[{indice}] {entrada['Data']}")
        print(entrada["Titulo"])
        print(entrada["Texto"])
        print()

def exibeEntradasHoje():

    today = datetime.now().strftime("%d/%m/%Y")
    encontrou = False

    for indice, entrada in enumerate(entradas, start=1) :

        if entrada["Data"] == today:
            encontrou = True

            print()
            print(f"[{indice}] {entrada['Data']}")
            print(entrada["Titulo"])
            print(entrada["Texto"])
            print()

    if not encontrou:
        print("Nenhuma entrada registrada hoje")
    

def pesquisarEntrada():

    pesquisa = input("Digite o que quer pesquisar:").strip().lower()
    encontrou = False

    for entrada in entradas:

        if pesquisa in entrada["Titulo"].lower() or pesquisa in entrada["Texto"].lower():
            encontrou = True

            print()
            print(entrada["Data"])
            print(entrada["Titulo"])
            print(entrada["Texto"])
            print()

    if not encontrou:
        print("Pesquisa não encontrada")

while True:
    menuDiario()
    opcao = input("Escolha sua opcao:")

    match opcao:
        case "1":
            titulo = input("Escreva o Título:")
            texto = input("Escreva o Texto da nota:")
            addEntrada(titulo, texto)

        case "2":
            exibeEntradasHoje()

        case "3":
            exibeEntradas()

        case "4":
            pesquisarEntrada()

        case "5":
            excluirEntrada()

        case "6":
            print("Tchau!")
            break

        case _:
            print("Opcão inválida, tente novamente")


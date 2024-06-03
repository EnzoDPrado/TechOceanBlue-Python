import time # Importa a biblioteca time para realizar uma pausa no código
import random # Importa a biblioteca random para gerar funcionalidades aleatórias

oceans = ['Oceano Atlântico', 'Oceano Índico', 'Oceano Pacífico'] # Lista dos oceanos que serão "explorados"
oceansTrashsFounded = [0, 0, 0] # Lista que contém a quantidade de lixo encontrado em cada índice correspondente à lista "oceans"
residueList = ["Pedra", "Peixe", "Lixo"] # Lista de resíduos que podem ser encontrados no oceano
oceansExploredIndex = [] # Lista para armazenar os índices dos oceanos já explorados

# Função para validar a entrada do usuário
def validateEntry(validEntrys, msg):
    # Laço de repetição para ficar repetindo até o usuario inserir uma opção valida
    while True:
        userEntry = input(msg)
        if not userEntry.isnumeric():
            continue
        else:
            userEntry = int(userEntry)

        # Laço de repetição para verificar se o dado inserido pelo usuario é uma das opções validas
        for i in range(len(validEntrys)):
            if int(userEntry) == validEntrys[i]:
                return userEntry

# Função para processar os resíduos encontrados
def findResidues(oceanResiduesList, selectedOceanIndex):
    # Laço para percorrer os resíduos encontrados e fazer as demais validações
    for i in range(len(oceanResiduesList)):
        print("Resíduo encontrado!")
        if oceanResiduesList[i] == "Lixo":
            oceansTrashsFounded[selectedOceanIndex] += 1
        time.sleep(0.3) # Pausa para simular a exploração real feita pelo find-bot
    print(f"Foram encontrados os seguintes resíduos:")
    for i in range(len(oceanResiduesList)): # Laço para mostrar os resíduos encontrados
        print(f"{i + 1} - {oceanResiduesList[i]}")
    print(f"E a seguinte quantidade de lixos: {oceansTrashsFounded[selectedOceanIndex]}")

# Função para gerar uma lista de índices aleatórios
def generateRandomIndexes(elements):
    quantity = random.randint(1, 15) # Gera um número aleatório de 1 a 25 para simular a quantidade de resíduos encontrados
    randomIndexes = random.choices(elements, k=quantity) # Utilização da biblioteca random para gerar índices aleatórios com base na lista de resíduos que podem ser encontrados
    return randomIndexes

print("|||||||||||||||||||||||||||||||||")
print(" |||| FIND-BOT INICIALIZADO ||||")
print("|||||||||||||||||||||||||||||||||")

# Laço para explorar cada oceano
for i in range(len(oceans)):
    validEntrys = []
    print('')
    for i in range(len(oceans)):
        if not (i in oceansExploredIndex): # Se o índice do oceano já foi explorado, não será uma opção válida para ser selecionado e também não será exibido na tela
            print(f'{i + 1} - {oceans[i]}')
            validEntrys.append(i + 1)

    oceanSelectedIndex = validateEntry(validEntrys, "Selecione um oceano para explorar com o find-bot: ") - 1
    oceansExploredIndex.append(oceanSelectedIndex)
    print(f"O find-bot está explorando o {oceans[oceanSelectedIndex]}\n")

    # Validação para verificar qual opção o usuário escolheu e inserir as demais validações
    if oceanSelectedIndex == 0:
        atlanticOceanResidues = generateRandomIndexes(residueList) # Chama a função random indexes para simular os resíduos encontrados pelo find-bot no respectivo oceano
        findResidues(atlanticOceanResidues, oceanSelectedIndex) # Chama a função que processa os resíduos encontrados
    elif oceanSelectedIndex == 1:
        indicOceanResidues = generateRandomIndexes(residueList)
        findResidues(indicOceanResidues, oceanSelectedIndex)
    elif oceanSelectedIndex == 2:
        pacificOceanResidues = generateRandomIndexes(residueList)
        findResidues(pacificOceanResidues, oceanSelectedIndex)

    # Verifica se o usuário deseja continuar explorando ou encerrar a aplicação
    if not (len(oceansExploredIndex) == 3):
        wantToContinue = validateEntry([1, 2], "\nDeseja continuar explorando ou deseja encerrar?\n1 - Continuar Explorando\n2 - Encerrar\n")
        if wantToContinue == 2:
            break

print("|||||||||||||||||||||||||||||||||")
print("    ||| FIND-BOT ENCERRADO |||   ")
print("|||||||||||||||||||||||||||||||||")
print("Resumo das explorações feitas pelo find-bot:")

# Resumo das explorações feitas
for i in range(len(oceansExploredIndex)):
    print(f"{oceans[oceansExploredIndex[i]]} - foram encontrado(s) {oceansTrashsFounded[oceansExploredIndex[i]]} lixo(s):")

areas = []      # Armazena áreas em metros quadrados
culturas = []   # Armazena tipo de cultura (Soja ou Café)
insumos = []    # Armazena quantidade de insumos em mL

def menu():                                                         
    print("\n=== Sistema de Gestão Agrícola ===")                   # Imprime o título do sistema
    print("1 - Cadastrar área")                                     # Opção para cadastrar nova área
    print("2 - Calcular insumos")                                   # Opção para calcular insumos
    print("3 - Mostrar dados")                                      # Opção para visualizar dados cadastrados
    print("4 - Deletar dados")                                      # Opção para atualizar registros
    print("5 - Atualizar dados")                                    # Opção para excluir registros
    print("6 - Sair")                                               # Opção para encerrar o programa
    return input("Escolha uma opção: ")                             # Solicita e retorna a escolha do usuário

def cadastrar_area():                                               # Função para cadastro da areas de cafe e soja
    print("\n=== Cadastro de Área ===")
    opcoes = {"1": "Soja", "2": "Café"}
    
    print("1 - Soja (NPK)")
    print("2 - Café (Fosfato)")
    
    cultura = input("Escolha a cultura (1 ou 2): ")
    if cultura not in opcoes:                                       # Verifica se a opção escolhida é válida
        print("Opção inválida!")
        return
    
    try:                                                            # Calculo da área
        comprimento = float(input("Comprimento (metros): "))
        largura = float(input("Largura (metros): "))
        area = comprimento * largura 
        
        areas.append(area)
        culturas.append(opcoes[cultura])
        insumos.append(0)                                           # O .append é como se você estivesse guardando uma nova informação em uma lista 
        
        print(f"Área cadastrada: {area} metros quadrados")
    except ValueError:                                              # Se o programa tenta fazer algo que não faz sentido ou não é permitido
        print("Por favor, digite valores numéricos válidos.")

def calcular_insumos():
    print("\n=== Cálculo de Insumos ===")
    if not areas:                                                   # Verifica se a lista está vazia
        print("Cadastre uma área primeiro!")
        return
    
    for i in range(len(areas)):                                     # Criei um Loop que percorre todas as áreas cadastradas, para cada área, calcula o insumo baseado na cultura
        insumos[i] = areas[i] * 500                                 # Defini que sao necessarios por padrão, 500mL por metro quadrado de ambos os insumos
        tipo_insumo = "Fosfato" if culturas[i] == "Café" else "NPK"
        print(f"Área {i+1} - {culturas[i]}: {insumos[i]}mL de {tipo_insumo}") # Montra o e o resultado do cálculo de cada insumo necessario para cada area

def mostrar_dados():                                                # Função para exibir todos os dados cadastrados
    print("\n=== Dados Cadastrados ===")
    if not areas:
        print("Sem dados cadastrados!")
        return
    
    for i in range(len(areas)):                                     # Denovo fiz um Loop que percorre todas as áreas cadastradas
        tipo_insumo = "Fosfato" if culturas[i] == "Café" else "NPK" # Verifica se culturas na posicao [i] na lista de culturas = "Café",  logo tipo_insumo será "Fosfato".
        print(f"\nÁrea {i+1}:")
        print(f"Cultura: {culturas[i]}")
        print(f"Área: {areas[i]}m²")
        print(f"Insumo necessário: {insumos[i]}mL de {tipo_insumo}")

def deletar_dados():
    print("\n=== Deletar Área ===")
                                                                    
    if not areas:                                                   # Verifica se há áreas cadastradas
        print("Nenhuma área cadastrada para deletar!")
        return
                  
    for i in range(len(areas)):                                     # Loop que percorre todas as áreas cadastradas
        tipo_insumo = "Fosfato" if culturas[i] == "Café" else "NPK" 
        print(f"{i+1} - {culturas[i]} - Área: {areas[i]}m² - Insumo: {insumos[i]}mL de {tipo_insumo}")  # Mostra dados de cada registro
      
    try:                                                            # O usuário digita o número da área que quer deletar. O -1 ajusta o número para o índice correto da lista (já que a lista começa em 0)
        indice = int(input("Digite o número da área para deletar (0 para cancelar): ")) - 1 
        
        if indice == -1:                                            # Se o usuário digitar 0, o índice ajustado será -1, e a função cancela a operação
            print("Operação cancelada!")
        elif 0 <= indice < len(areas):  
            areas.pop(indice)                                       # Se o índice estiver dentro dos limites da lista, a área é removida com areas.pop(indice) O .pop() remove um elemento de uma lista com base no índice.
            print("Área deletada com sucesso!")
        else:  
            print("Número de área inválido!")
    except ValueError:                                              # Se o usuário não digitar um número valido
         print("Por favor, digite um número válido!")

def atualizar_dados():
    print("\n=== Atualizar Dados ===")
    
    if not areas:                                                   # Verifica se há áreas cadastradas
        print("Nenhuma área cadastrada para atualizar!")
        return
    
    for i, area in enumerate(areas):                                # Usa a função enumerate para mostrar cada área com um número (começando em 1), o tipo de cultura e o tamanho da área
        print(f"{i+1} - Cultura: {culturas[i]} - Área: {area}m²")
    
    try:
        indice = int(input("Digite o número da área para atualizar (0 para cancelar): ")) - 1     # Pede ao usuário para escolher qual área atualizar, assim como na funcao de deletar, o -1 ajusta o número para o índice correto da lista
        
        if indice == -1:                                            # Usuário digitou 0 (cancelar assim como na funcao de deletar)
            print("Operação cancelada!")
        elif 0 <= indice < len(areas):                              # Índice válido
            print("\nO que você deseja atualizar?")                 
            print("1 - Tamanho da área")
            print("2 - Tipo de cultura")
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":                                        # Atualizar tamanho da área
                try:
                    novo_tamanho = float(input("Novo tamanho da área (metros quadrados): "))
                    areas[indice] = novo_tamanho
                    print("Tamanho da área atualizado com sucesso!")
                except ValueError:
                    print("Por favor, digite um valor numérico válido.")
            
            elif opcao == "2":                                      # Atualizar tipo de cultura
                print("1 - Soja")
                print("2 - Café")
                nova_cultura = input("Escolha a nova cultura (1 ou 2): ")
                
                if nova_cultura == "1":
                    culturas[indice] = "Soja"
                    print("Cultura atualizada para Soja!")
                elif nova_cultura == "2":
                    culturas[indice] = "Café"
                    print("Cultura atualizada para Café!")
                else:
                    print("Opção inválida!")
            else:
                print("Opção inválida!")
        else:                                                       # Índice inválido
            print("Número de área inválido!")
    except ValueError:                                              # Se o usuário não digitar um número
        print("Por favor, digite um número válido!")

while True:                                                         # Loop infinito que mantem o programa em execução 
    opcao = menu()
    
    if opcao == "1":
        cadastrar_area()
    elif opcao == "2":
        calcular_insumos()
    elif opcao == "3":
        mostrar_dados()
    elif opcao == "4":
        deletar_dados()
    elif opcao == "5":
        atualizar_dados()
    elif opcao == "6":
        print("Programa encerrado!")
        break
    else:
        print("Opção inválida! Por favor, escolha uma opção de 1 a 6.")
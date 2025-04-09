# Função que exibe uma mensagem de boas-vindas inicial ao usuário
def tela_bem_vindo():
    """
    Exibe uma mensagem inicial de boas-vindas.
    Informa os recursos principais do sistema e orienta o usuário no uso do menu.
    """
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("          Bem-vindo ao Sistema de Ordens")
    print("             de Serviço e Dispositivos")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("\nEste sistema permite gerenciar:\n")
    print("- Ordens de Serviço")
    print("- Dispositivos como Notebooks, Computadores e Consoles\n")
    print("Por favor, selecione uma das opções disponíveis no menu.")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")


# Classe básica para representar um Dispositivo genérico
class Dispositivo:
    """
    Classe para representar um dispositivo genérico.
    Serve como base para diferentes tipos de dispositivos, como computadores, consoles, etc.
    """

    def __init__(self, tipo, identificador1, identificador2, problema_reportado):
        """
        Inicializa um dispositivo com os atributos fornecidos.
        :param tipo: Tipo do dispositivo (Ex.: Notebook, Computador, Console)
        :param identificador1: Identificador único do dispositivo, como número de série
        :param identificador2: Outro identificador para distinção adicional
        :param problema_reportado: Breve descrição do problema encontrado no dispositivo
        """
        self.tipo = tipo
        self.identificador1 = identificador1
        self.identificador2 = identificador2
        self.problema_reportado = problema_reportado

    def descricao(self):
        """
        Exibe uma descrição detalhada do dispositivo.
        Essa função é útil para fornecer informações sobre o dispositivo ao cliente ou técnico.
        """
        return f"Tipo: {self.tipo}\n" \
               f"Identificador 1: {self.identificador1}\n" \
               f"Identificador 2: {self.identificador2}\n" \
               f"Problema Reportado: {self.problema_reportado}"


# Exemplo de uma função principal modularizada (menu principal do sistema)
def menu():
    """
    Exibe o menu principal do sistema.
    Gerencia as interações com o usuário para acessar as funcionalidades do programa.
    """
    while True:
        print("\nMenu Principal:")
        print("1. Registrar uma nova ordem de serviço")
        print("2. Atualizar o status de uma ordem")
        print("3. Listar todas as ordens")
        print("4. Sair")

        # Coleta e trata a opção selecionada pelo usuário
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            registrar_ordem()
        elif opcao == '2':
            atualizar_status()
        elif opcao == '3':
            listar_ordens()
        elif opcao == '4':
            print("Encerrando o programa. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")


# Suporte para registrar uma nova ordem de serviço
def registrar_ordem():
    """
    Permite o registro de uma nova ordem de serviço no sistema.
    Implementação prática que coleta informações sobre o cliente e o dispositivo.
    """
    print("\n** Registrar Nova Ordem de Serviço **")
    # Exemplo de coleta de dados para criação de uma ordem
    cliente = input("Digite o nome do cliente: ")
    tipo_dispositivo = input("Qual o tipo do dispositivo? (Notebook, Computador, Console): ")
    identificador1 = input("Informe o identificador 1 (Número de Série): ")
    identificador2 = input("Informe o identificador 2 (Código Adicional): ")
    problema = input("Descreva o problema do dispositivo: ")

    # Aqui seria possível criar e registrar a ordem com base nos dados fornecidos
    print("\nOrdem registrada com sucesso!")
    print(f"Cliente: {cliente}")
    print(f"Dispositivo: {tipo_dispositivo}")
    print(f"Problema: {problema}")


# Suporte para atualizar o status de uma ordem existente
def atualizar_status():
    """
    Atualiza o status de uma ordem existente com base no número da ordem informado.
    """
    print("\n** Atualizar Status de Ordem **")
    # Exemplo rápido para o processo
    numero_ordem = input("Informe o número da ordem: ")
    novo_status = input("Informe o novo status (Ex.: Em andamento, Concluído, Aguardando peça): ")
    print(f"O status da ordem {numero_ordem} foi atualizado para '{novo_status}'!")


# Suporte para listar ordens existentes no sistema
def listar_ordens():
    """
    Lista todas as ordens de serviço disponíveis no sistema.
    """
    print("\n** Lista de Ordens de Serviço **")
    # Exemplo rápido - Aqui poderia se conectar a um banco de dados ou outro armazenamento
    print("1. Ordem 001 - Cliente: João - Status: Concluído")
    print("2. Ordem 002 - Cliente: Maria - Status: Em Andamento")
    print("3. Ordem 003 - Cliente: Mariana - Status: Aguardando peça")


# Função principal que inicia o programa chamando a tela de boas-vindas e o menu
def main():
    """
    Ponto de entrada principal do sistema.
    Exibe uma tela de boas-vindas e redireciona para o menu principal.
    """
    tela_bem_vindo()  # Exibe a tela inicial de boas-vindas
    menu()  # Abre o menu principal


# Garante que o programa execute a função main ao ser executado diretamente
if __name__ == "__main__":
    main()

class TabelaHash:
    def __init__(self, tamanho, metodo_hash, tratamento_colisao):
        # Inicializa a tabela hash com os parâmetros fornecidos
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)] # Cria uma lista de listas (bucket) do tamanho especificado
        self.metodo_hash = metodo_hash # Define o método de hash
        self.tratamento_colisao = tratamento_colisao # Define o método de tratamento de colisão

    def hash_divisao(self, nome):
        # Método de hash usando a técnica da divisão
        return sum(ord(c) for c in nome) % self.tamanho

    def hash_dobra(self, nome):
        # Método de hash usando a técnica da dobra
        nome_binario = ''.join(format(ord(c), '08b') for c in nome)  # Converte cada caractere para binário
        metade = len(nome_binario) // 2 # Divide o binário em duas partes
        part1 = int(nome_binario[:metade], 2) # Converte a primeira metade para inteiro
        part2 = int(nome_binario[metade:], 2) # Converte a segunda metade para inteiro
        return (part1 + part2) % self.tamanho # Soma as partes e aplica o módulo com o tamanho da tabela

    def hash_multiplicacao(self, nome):
         # Método de hash usando a técnica da multiplicação
        A = (5**0.5 - 1) / 2 # Constante A (razão áurea)
        valor = sum(ord(c) for c in nome) # Soma os valores ASCII dos caracteres do nome
        return int(self.tamanho * ((valor * A) % 1)) # Multiplica por A, pega a parte fracionária e escala para o tamanho da tabela 

    def calcular_indice(self, nome):
        # Calcula o índice na tabela hash usando o método de hash selecionado
        if self.metodo_hash == 'divisao':
            return self.hash_divisao(nome)
        elif self.metodo_hash == 'dobra':
            return self.hash_dobra(nome)
        elif self.metodo_hash == 'multiplicacao':
            return self.hash_multiplicacao(nome)

    def adicionar(self, nome):
        # Adiciona um nome na tabela hash
        indice = self.calcular_indice(nome)
        if self.tratamento_colisao == 'encadeamento':
            # Tratamento de colisão por encadeamento
            self.tabela[indice].append(nome)
        else:
            # Tratamento de colisão por endereçamento aberto
            for i in range(self.tamanho):
                novo_indice = (indice + i) % self.tamanho
                if not self.tabela[novo_indice]: # Encontra o próximo índice disponível
                    self.tabela[novo_indice].append(nome)
                    return

    def buscar(self, nome):
        # Busca um nome na tabela hash
        indice = self.calcular_indice(nome)
        if self.tratamento_colisao == 'encadeamento':
            # Busca no bucket correspondente
            return nome in self.tabela[indice]
        else:
            # Busca por endereçamento aberto
            for i in range(self.tamanho):
                novo_indice = (indice + i) % self.tamanho
                if nome in self.tabela[novo_indice]:
                    return True
        return False

    def remover(self, nome):
        # Remove um nome da tabela hash
        indice = self.calcular_indice(nome)
        if self.tratamento_colisao == 'encadeamento':
            # Remoção no encadeamento
            if nome in self.tabela[indice]:
                self.tabela[indice].remove(nome)
        else:
            # Remoção no endereçamento aberto
            for i in range(self.tamanho):
                novo_indice = (indice + i) % self.tamanho
                if nome in self.tabela[novo_indice]:
                    self.tabela[novo_indice].remove(nome)
                    return

    def exibir(self):
        # Exibe a tabela hash
        for i, lista in enumerate(self.tabela):
            print(f"Índice {i}: {lista}")


def main():
    # Função pincipal, interage com o usuário para configurar e operar a tabela hash, permitindo adicionar, buscar, remover e exibir nomes, além de encerrar o programa.
    print("Bem-vindo ao programa de Tabela Hash!")
    tamanho = int(input("Digite o tamanho da tabela hash: "))
    metodo_hash = input("Escolha o método hash (divisao, dobra, multiplicacao): ").lower()
    tratamento_colisao = input("Escolha o tratamento de colisões (encadeamento, enderecamento): ").lower()

    tabela_hash = TabelaHash(tamanho, metodo_hash, tratamento_colisao)

    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar nome")
        print("2. Buscar nome")
        print("3. Remover nome")
        print("4. Exibir tabela hash")
        print("5. Sair")
        opcao = int(input("Opção: "))

        if opcao == 1:
            nome = input("Digite o nome para adicionar: ")
            tabela_hash.adicionar(nome)
        elif opcao == 2:
            nome = input("Digite o nome para buscar: ")
            encontrado = tabela_hash.buscar(nome)
            if encontrado:
                print(f"Nome '{nome}' encontrado na tabela hash.")
            else:
                print(f"Nome '{nome}' não encontrado na tabela hash.")
        elif opcao == 3:
            nome = input("Digite o nome para remover: ")
            removido = tabela_hash.buscar(nome)
            if removido:
                tabela_hash.remover(nome)
                print(f"Nome '{nome}' removido da tabela hash.")
            else:
                print(f"Nome '{nome}' não encontado na tabela hash")   
            
        elif opcao == 4:
            tabela_hash.exibir()
        elif opcao == 5:
            print("====== Programa Encerrado ======")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

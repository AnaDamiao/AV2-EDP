class TabelaHash:
    def __init__(self, tamanho, metodo_hash, tratamento_colisao):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]
        self.metodo_hash = metodo_hash
        self.tratamento_colisao = tratamento_colisao

    def hash_divisao(self, nome):
        return sum(ord(c) for c in nome) % self.tamanho

    def hash_dobra(self, nome):
        nome_binario = ''.join(format(ord(c), '08b') for c in nome)
        metade = len(nome_binario) // 2
        part1 = int(nome_binario[:metade], 2)
        part2 = int(nome_binario[metade:], 2)
        return (part1 + part2) % self.tamanho

    def hash_multiplicacao(self, nome):
        A = (5**0.5 - 1) / 2
        valor = sum(ord(c) for c in nome)
        return int(self.tamanho * ((valor * A) % 1))

    def calcular_indice(self, nome):
        if self.metodo_hash == 'divisao':
            return self.hash_divisao(nome)
        elif self.metodo_hash == 'dobra':
            return self.hash_dobra(nome)
        elif self.metodo_hash == 'multiplicacao':
            return self.hash_multiplicacao(nome)

    def adicionar(self, nome):
        indice = self.calcular_indice(nome)
        if self.tratamento_colisao == 'encadeamento':
            self.tabela[indice].append(nome)
        else:
            for i in range(self.tamanho):
                novo_indice = (indice + i) % self.tamanho
                if not self.tabela[novo_indice]:
                    self.tabela[novo_indice].append(nome)
                    return

    def buscar(self, nome):
        indice = self.calcular_indice(nome)
        if self.tratamento_colisao == 'encadeamento':
            return nome in self.tabela[indice]
        else:
            for i in range(self.tamanho):
                novo_indice = (indice + i) % self.tamanho
                if nome in self.tabela[novo_indice]:
                    return True
        return False

    def remover(self, nome):
        indice = self.calcular_indice(nome)
        if self.tratamento_colisao == 'encadeamento':
            if nome in self.tabela[indice]:
                self.tabela[indice].remove(nome)
            else:
                print(f"Nome não consta na base")
        else:
            for i in range(self.tamanho):
                novo_indice = (indice + i) % self.tamanho
                if nome in self.tabela[novo_indice]:
                    self.tabela[novo_indice].remove(nome)
                    return

    def exibir(self):
        for i, lista in enumerate(self.tabela):
            print(f"Índice {i}: {lista}")


def main():
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

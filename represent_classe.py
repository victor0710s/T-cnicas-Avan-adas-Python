# Personalizando representações string de classes


class Pessoa():
    def __init__(self):
        self.nome = "Victor"
        self.sobrenome = "Silva"
        self.idade = 20

    # TODO: Use __repr__ para criar uma string que seja útil para debug

    def __repr__(self):
        txt = "<Classe Pessoa - nome: {0}, sobrenome: {1}, idade: {2}>"
        return txt.format(self.nome, self.sobrenome, self.idade)

    # TODO: Use __str__ para criar uma string amigável para humanos
    def __str__(self):
        txt = "Pessoa {0} {1}, tem {2} anos."
        return txt.format(self.nome, self.sobrenome, self.idade)

    # TODO: Use bytes para converter a string em um objeto bytes
    def __bytes__(self):
        para_bytes = 'Pessoa: {0}:{1}:{2}'.format(
            self.nome, self.sobrenome, self.idade
        )
        return para_bytes.encode('utf-8')


def main():
    # Criando uma instância de Pessoa
    pessoa = Pessoa()

    # Usando as funções embutidas de Python para representar a pessoa
    # em uma string
    print(repr(pessoa))
    print(str(pessoa))
    print('Formatado: {0}'.format(pessoa))
    print(bytes(pessoa))


if __name__ == '__main__':
    main()

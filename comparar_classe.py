# Usando métodos mágicos para comparar objetos entre si


class Pessoa():
    def __init__(self, nome, sobrenome, nivel, anos_trabalhando):
        self.nome = nome
        self.sobrerenome = sobrenome
        self.nivel = nivel
        self.senioridade = anos_trabalhando

    # TODO: Implemente as comparções usando nível de cada pessoa
    def __ge__(self, other):  # Maior ou igual
        if self.nivel == other.nivel:
            return self.senioridade >= other.senioridade
        return self.nivel >= other.nivel

    def __gt__(self, other):  # Maior que
        if self.nivel == other.nivel:
            return self.senioridade > other.senioridade
        return self.nivel > other.nivel

    def __lt__(self, other):  # Menor que
        if self.nivel == other.nivel:
            return self.senioridade < other.senioridade
        return self.nivel < other.nivel

    def __le__(self, other):  # Menor ou igual
        if self.nivel == other.nivel:
            return self.senioridade <= other.senioridade
        return self.nivel <= other.nivel


def main():
    # Definindo pessoas
    dpto = []
    dpto.append(Pessoa("Túlio", "Toledo", 5, 9))
    dpto.append(Pessoa("João", "Junior", 4, 12))
    dpto.append(Pessoa("Jessica", "Temporal", 6, 6))
    dpto.append(Pessoa("Rebeca", "Robinson", 5, 13))
    dpto.append(Pessoa("Thiago", "Tavares", 5, 12))

    # TODO: Descobrindo quem é mais sênior
    print(dpto[0] > dpto[2])
    print(dpto[4] < dpto[3])

    # TODO: Organizando as pessoas por senioridade
    pessoas = sorted(dpto)
    for pessoa in pessoas:
        print('-', pessoa.nome)


if __name__ == '__main__':
    main()

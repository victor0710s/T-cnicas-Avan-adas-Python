# TODO: Defina uma função que recebe argumentos variáveis
def adicao(*args):
    return sum(args)


def main():
    # TODO: Passe argumentos diferentes para o método adição()
    print(adicao(10, 20, 5, 15))
    print(adicao(1, 2, 3))

    # TODO: Passe uma lista para o método adicao()
    valores = [10, 20, 5, 15]
    print(adicao(*valores))


if __name__ == "__main__":
    main()

# Demonstrate built-in utility functions


def main():
    # TODO: Use any() e all() para testar valores booleanos
    lista = [1, 5, 2, 0, 4, 2]

    # TODO: A função any() vai retornar True caso qualquer valor da lista
    # seja verdade (!= 0)

    print(any(lista))

    # TODO: A função all() vai retornar True apenas se todos os
    # valores da lista forem verdade

    print(all(lista))  # False, pois tem o 0 na lista

    # TODO: As funções min e max retornam os valores minimo e máximo
    # respectivamente

    print('Minimo:', min(lista))
    print('Máximo:', max(lista))

    # TODO: Use a função sum() para somar todos os valores da lista

    print('Total:', sum(lista))


if __name__ == "__main__":
    main()

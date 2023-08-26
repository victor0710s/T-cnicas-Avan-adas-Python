# Usando funções transformadoras: sorted, filter, map


def primeiro_filtro(x):
    if x % 2 == 0:
        return False
    return True


def segundo_filtro(x):
    if x.isupper():
        return False
    return True


def quadrado(x):
    return x ** 2
    # return pow(x, 2)


def nota_para_conceito(x):
    match x:  # Função nova na versao 3.9 em diante
        case x if x >= 90:
            return 'A'

        case x if x >= 80:
            return 'B'

        case x if x >= 70:
            return 'C'

        case x if x >= 65:
            return 'D'

        case _:
            return 'F'


def main():
    # Definindo sequências para usarmos nesta tarefa
    numeros = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    letras = 'abcDeFGHiJklmnoP'
    notas = (81, 89, 94, 78, 61, 66, 99, 74)

    # TODO: Use filter para remover itens de uma lista
    # filter(função, lista/itens...)
    impares = list(filter(primeiro_filtro, numeros))
    # print(impares)

    # TODO: Use filter numa sequência de caracteres
    minusculas = list(filter(segundo_filtro, letras))
    # print(minusculas)

    # TODO: Use map para criar uma nova sequência de valores
    square = list(map(lambda x: x ** 2, numeros))  # lambda ou função comum
    # print(square)

    # TODO: Use sorted e map para mudar as notas para conceito
    notas = sorted(notas)
    conceito = list(map(nota_para_conceito, notas))
    print(conceito)


if __name__ == "__main__":
    main()

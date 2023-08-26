# Usando docstrings para documentar métodos


def minha_funcao(arg1, arg2=None):
    # TODO: escrever a docstring para essa função
    '''Minha função que faz um print dos argumentos passados.

    Params:
        arg1: primeiro argumento, algo intessante.
        arg2: segundo argumento, Default: None.

    '''
    print(arg1, arg2)


def main():
    print(minha_funcao.__doc__)


if __name__ == '__main__':
    main()

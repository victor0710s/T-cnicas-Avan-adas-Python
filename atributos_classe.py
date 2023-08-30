# Personalizando a representação string de uma classe


from typing import Any


class MinhasCores():
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100

    # TODO: Use getattr para retornar um valor de forma dinâmica

    def __getattr__(self, attr):
        if attr == 'rgb':
            return (self.red, self.green, self.blue)
        else:
            raise AttributeError

    # TODO: Use setattr para retornar um valor de forma dinâmica

    def __setattr__(self, attr, val):
        if attr == 'rgb':
            self.red = val[0]
            self.green = val[1]
            self.blue = val[2]
        else:
            super().__setattr__(attr, val)

    # TODO: Use dir para listar os atributos disponíveis

    def __dir__(slef):
        return ('red', 'green', 'blue', 'rgb')


def main():
    # Criando uma instância de MinhasCores
    cores = MinhasCores()

    # TODO: Mostre o valor de um atributo
    print(cores.rgb)

    # TODO: Defina o valor de um atributo
    cores.rgb = (125, 200, 86)
    print(cores.rgb)

    # TODO: Acesse um atributo específico
    print(cores.red)

    # TODO: Liste os atributos disponíveis
    print(dir(cores))


if __name__ == '__main__':
    main()

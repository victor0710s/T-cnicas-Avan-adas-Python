# Uso de objetos namedtuple
import collections


def main():
    # TODO> Crie uma namedtuple para armazenar coodernadas
    coordenadas = collections.namedtuple('Coordenadas', 'x y')

    p1 = coordenadas(10, 20)
    p2 = coordenadas(30, 40)

    print(p1, p2, sep='\n')
    print(p1.x, p1.y)

    # TODO: Use _replace() para criar uma instância nova
    p1 = p1._replace(x=100)
    print('Novo valor:', p1)


if __name__ == '__main__':
    main()

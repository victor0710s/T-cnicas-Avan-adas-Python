# Strings e bytes não são diretamente intercambiáveis
# Strings contém unicode, bytes são valores de 8bits


def main():
    # Definindo alguns valores iniciais
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b)

    s = 'Isto é uma string'
    print(s)

    # TODO: Tentar juntar os dois valores
    # print(s + b) # Não é possivel concatenar str com bytes

    # TODO: Bytes e str precisam ser apropriamente encoded ou decoded
    print(s + b.decode('utf-8'))

    # TODO: Fazendo o encode da str como UTF-32
    print(s.encode('utf-32'))


if __name__ == '__main__':
    main()

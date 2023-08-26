# Usando lambdas como funções de uma linha


def celsius_para_fahrenheit(temp):
    return (temp * 9/5) + 32


def fahrenheit_para_celsius(temp):
    return (temp - 32) * 5/9


def main():
    temp_em_c = [0, 12, 34, 100]
    temp_em_f = [32, 65, 100, 212]

    # TODO: Defina funções tradicionais para converter as temperaturas
    print(list(map(celsius_para_fahrenheit, temp_em_c)))
    print(list(map(fahrenheit_para_celsius, temp_em_f)))

    # TODO: Use lambdas para coverter as temperaturas
    print(list(map(lambda temp: (temp * 9/5) + 32, temp_em_c)))
    print(list(map(lambda temp: (temp - 32) * 5/9, temp_em_f)))


if __name__ == "__main__":
    main()

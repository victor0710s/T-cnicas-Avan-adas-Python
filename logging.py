# Use o módulo logging

# TODO: Use o módulo embutido logging
import logging


def main():
    # TODO: Use basicConfig para configurar seu logging
    logging.basicConfig(level=logging.DEBUG,
                        filename='output.log')

    # Testando cada um dos níveis de log
    logging.debug("Esta é uma mensagem de debug!")
    logging.info("Esta é uma mensagem de informação!")
    logging.warning("Esta é uma mensagem de aviso!")
    logging.error("Esta é uma mensagem de erro!")
    logging.critical("Esta é uma mensagem de crítica!")

    # TODO: Use string para formartar o log


if __name__ == '__main__':
    main()

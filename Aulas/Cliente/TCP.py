import socket
import sys


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as erro:
        print("A conexão falhou!!!")
        print("Erro: {}".format(erro))
        sys.exit()

    print("Socket criado com seucesso!")

    host_alvo = input("Digite hot ou ip a ser conectado: ")
    porta_alvo = input("Digite a porta a ser conectada: ")

    try:
        s.connect((host_alvo, int(porta_alvo)))
        print("Cliente TCP conectado com seucesso no Host: " +
              host_alvo + " e na Porta: " + porta_alvo)
        s.shutdown(2)

    except socket.error as erro:
        print("Não foi possivel conectar no Host: " +
              host_alvo + " e na Porta: " + porta_alvo)
        print("Erro: {}".format(erro))
        sys.exit()


if __name__ == "__main__":
    main()

def boasVindas(nome, idade):
    print("olá {}, nem parece que você tem {} anos".format(nome, idade))

if __name__ == "__main__":
    nome = input("Qual o seu nome? ")
    idade = int(input("Qual sua idade? "))
    boasVindas(nome, idade)

print("*porta de entrada*")

while True:
    nome = input("coloque seu nome aqui: ").strip().lower()
    lista_nomes = ["karlos", "paloma", "bernadino", "rafael", "nicolas",]
    if nome in [n.lower() for n in lista_nomes]:
        print("acesso liberado!!")
        break
    else:
        print("acesso negado tente novemente")
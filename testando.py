nome = input("Digite seu nome: ")
print("Olá", nome,)
while True:
    pergunta = input("Tudo bem?").strip().lower()
    if pergunta == "sim":
        print("que bom!!")
        break
    elif pergunta == "não":
        print("que pena, tomare que seu dia melhore")
        break
    print("por favor repita com (sim ou não)")
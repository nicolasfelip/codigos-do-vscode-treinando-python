print("calculadora fodona")
a = int(input("insira um valor:"))
b = int(input("insira outro valor:"))
escolha = input("escolha em so = soma, mul = multiplicação, sub = subtração e div = divisão: ").strip().lower()
if escolha == "so":
    resultado = a + b
elif escolha =="mul":
    resultado = a * b
elif escolha =="sub":
    resultado = a - b
elif escolha =="div":
   resultado =  a / b
print("aqui está o seu resultado", resultado)
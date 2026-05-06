numeros = []
for i in range(6):
    valor = float(input("digite um numero:"))
    if(valor <0):
        valor = 1
    numeros.append(valor)
    print("lista de resultados: ", numeros)
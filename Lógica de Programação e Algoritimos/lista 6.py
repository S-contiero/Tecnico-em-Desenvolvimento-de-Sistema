numeros = []
maior = -9999999999999999999999
for i in range(5):
    numeros.append(int(input("Digite um numero:")))
for numero in numeros:
    if(numeros > maior):
        maior = numero
print("Maior: ", maior)


vetor = []
numero = []
contador = []
for i in range(8):
    num = int(input("Digite um número:"))
    vetor.append(num)

num_digitado = int(input("Digite um numero pra procurar no vetor: "))

for i in range(8):
    if(vetor[i] == num_digitado):
        print("encontrou")
#Revisão vetores - 1
#Solicitar ao usuario a quantidade de numeros
#Preencher o vetor 
#Percorrer o vetor e calcular a soma dos numeros 
#Exibir a soma
----------------------------------------------------------------------------------------------------------------------------------
#Passo 1 - criar as variaveis 
numero = int(input("Digite quantidade de numeros: "))
vetor = []
soma = 0

#Passo 2 - preencher o vetor
for i in range(numero):
    vetor.appende(int(input("Digite um numero: ")))

#Passo 3 - percorrer o vetor 
for num in vetor:
    soma = soma + num

print("A soma é: ", soma)


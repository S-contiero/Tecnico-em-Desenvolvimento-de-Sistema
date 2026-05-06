#criando uma variavel numero 
numero = 10
#criando uma variavel textual
nome = "Stefany"
#usuario inserir um texto 
nome_completo = input("Digite um numero: ")
#usuario inserir um numero inteiro 
idade = int(input("Digite sua idade: "))
#usuario inserir um numero decimal 
salario = float(input("Digite seu salario: "))

#estruturas condicionais - if
if(salario > 1500 and idade > 18):
    print("Você pode tirar carta!")
elif(salario < 1500 or idade < 18):
    print('Você nao pode tira carta!')
else:
    print("Invalido")

#estrura condicionais exemplo 2
turno = input("Digite seu turno (M/V/N): ")
if (turno == "M"): #utilize dois iguais para cpmparar 
    print("Bom dia!")
elif(turno == "V"):
    print("Boa tarde!")
elif(turno == "N"):
    print("Boa noite!")
else:#else nao tem parenteses 
    print("Invalio")

#estrutura de repetiço~es 
# 0 -> 10
for i in range (11): #sempre colocar mais um 
    print(i)

#5 -> 65(aumentando de 5 em 5)
for i in range(5,66,+5):
    print(i)

#1 -> 15
for i in range (1,16): #vai ate o 15
    print(i)

#122 -> 0 (tirando de 2 em 2)
for i in range (122,-1,-2):
    print(i)

#usuarios escolhe o inicio e fim
#inicio > fim
inicio = int(input("inicio: "))
fim = int(input("fim: "))
for i in range (inicio, fim+1):
    print(i)

#vetors 
nomes = []
#sempre uilizar preencher o vetor
for i in range (5)  
    nomes.append(input("Digite um nome: "))
#sempre utilizar para exibir o vetor
for nome in nomes:
    print(nome)
          


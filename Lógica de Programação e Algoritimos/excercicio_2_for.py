numero1 = int(input("Digite o primeiro numero:"))
numero2 = int(input("Digite o segundo numero:"))
soma = 0 

for i in (numero1,numero2+1):
    if(i%2 == 0):
        soma = soma + i
    
print(soma)
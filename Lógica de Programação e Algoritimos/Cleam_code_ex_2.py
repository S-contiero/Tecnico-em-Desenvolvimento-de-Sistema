idade = int(input("Digite sua idade: "))

if (idade >= 18):
    print("Voce é maior de idade")
elif (idade >= 0 and idade < 18):
    print("Voce é de menor")
else:
    print("idade invalida")
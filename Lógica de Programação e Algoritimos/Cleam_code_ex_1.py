numeros = []

for i in range(5):
    numeros.append(int(input(f"Digite a {i+1}ª numero: ")))

soma = sum(numeros)
print("A soma é: ", soma)

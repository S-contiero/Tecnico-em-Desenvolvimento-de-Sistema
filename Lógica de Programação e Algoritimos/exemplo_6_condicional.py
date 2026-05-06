valoeCompra = float(input("Digite o valor da compra:"))
cupomDesconto = input("Possui cupomde desconto? ")

if(valoeCompra >= 200 or cupomDesconto == "Sim"):
    print("Você ganhou um desconto de 15%!")
else:
    print("Você nao tem direito a descontos no momento!")
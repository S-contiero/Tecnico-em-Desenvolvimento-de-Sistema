lado1 = int(input("Digite o lado1:"))
lado2 = int(input("Digite o lado2:"))
lado3 = int(input("Digite o lado2:"))

if((lado1 + lado2) >lado3 and (lado1 + lado3) >lado2 and (lado2 + lado3) >lado1):
    if(lado1 == lado2 and lado2 == lado3 and lado3 == lado1):
        print("equilatero")
    elif(lado1 != lado2 and lado2 != lado3 and lado3 != lado1):
        print("escaleno")
    else:("isosceles")
else:
    print("O triangulo não existe!")
programa {
  funcao inicio() {
    inteiro lado1, lado2, ladoe

    escrva("Digite o lado:")
    leia(lado1)

    escreva("Digite o lado:")
    leia(lado2)

    escreva("Digite o lado:")
    leia(lado3)

    se(lado1 == lado2 e lado2 == lado2 e lado3 == lado1){
      escreva("equilatero")
    }
    senao se(lado1 == lado2 ou lado2 == lado3 ou lado3 == lado1){
      escreva("isosceles")
    }
    senao se(lado1 != lado2 e lado2 != lado3 e lado3 != lado1){
      escreva("escaleno")
    }
  
  }
}

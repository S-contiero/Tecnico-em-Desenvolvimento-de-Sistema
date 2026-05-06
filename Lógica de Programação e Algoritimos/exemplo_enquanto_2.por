programa {
  funcao inicio() {
    cadeia resposta = "sim"

    enquanto(resposta == "sim"){
      escreva("\n Esta chovendo?")
      leia(resposta)

      se(resposta == "sim"){
        escreva("\n Leve um gurda-chuva!☔")
      }
    }
  }
}

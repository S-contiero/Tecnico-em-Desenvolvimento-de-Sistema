notas = []

for i in range(4):
    #tenta solicitar as notas
    try:
        nota = float(input(f"Digite a {i+1}ª nota: "))

        if(nota < 0 or nota > 10):
            print("Nota invalida. Insira um valor entre 0 e 10!")
            exit()
        else:
            notas.append(nota)
    #Se tiver algum erro (execessão) de valor, retorna uma mensagem
    except ValueError:
        print("Erro: Inserir um número válido!")

if not notas:
    print("Erro: nenhuma nota foi enserida!")
else:
    media = sum(notas)/len(notas)
    if(media >= 7):
        print(F"Média = {media} - aprovada!")
    elif(media >= 5):
        print(f"Média = {media} - recuperção!")
    else:
        print(f"Média = {media} - reprovado!")
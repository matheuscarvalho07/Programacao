#Objetivo: Criar um programa que printe os numeros de uma lista e, depois, eles multiplicados por 2
#Bonus: Colocar os numeros multiplicados em uma outra lista e printa-la

lista = [2,3,7,12,2]

lista_multiplicada = [2,3,7,12,2]




for i in range(len(lista)):
    valor = lista[i]
    posicao = i + 1
    print(f"A posição do {posicao}º valor da lista é {valor}")

print("Números multiplicados por 2:")
for numero in lista_multiplicada:
    print(numero*2)
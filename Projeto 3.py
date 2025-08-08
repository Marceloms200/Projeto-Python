#Programa que irá calcular a média do aluno baseado nas suas notas.
nota_1 = float(input("Qual é a sua primeira nota?"))
nota_2 = float(input("Qual é a sua segunda nota?"))
nota_3 = float(input("Qual é a sua terceira nota?"))
media = (nota_1 + nota_2 + nota_3) / 3
print(f"A sua média é {media:.2f}")
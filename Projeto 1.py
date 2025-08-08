nome = input("Qual é o seu nome?")
nascimento = int(input("Em que ano você nasceu?"))
faculdade = input("Em qual instituição você estuda?")
curso = input("Qual o seria o curso que está realizando neste momento?")
idade = 2025 - nascimento
print(f"Olá {nome.capitalize()},você fará {idade} anos de idade, está realizando a faculdade na {faculdade.capitalize()}, realizando o curso de {curso}.")
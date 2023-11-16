nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))

print("A primeira nota é: {}\n"
      "A segunda nota é: {}\n"
      "A media é: {:.2f}"
      .format(nota1, nota2, ((nota1 + nota2) / 2)))

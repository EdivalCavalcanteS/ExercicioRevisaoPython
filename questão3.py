cont=0

pergunta1= input(" Telefonou para a v�tima? Sim ou N�o:")

if pergunta1 == 'Sim':
  cont = cont + 1

pergunta2= input("Esteve no local do crime?  Sim ou N�o:")

if pergunta2 == 'Sim':
  cont = cont + 1

pergunta3= input("Mora perto da v�tima? Sim ou N�o:")

if pergunta3 == 'Sim':
  cont = cont + 1

pergunta4= input("Devia para a v�tima?  Sim ou N�o:")

if pergunta4 == 'Sim':
  cont = cont + 1

pergunta4= input("J� trabalhou com a v�tima Sim ou N�o:")

if pergunta4 == 'Sim':
  cont = cont + 1


if cont == 2:
  print("Suspeita(o) ._.")

if cont == 3 or cont == 4:
  print ("C�mplice :/")

if cont == 5:
  print ("Assassino(a) :(")

if cont == 0:
  print( "Inocente ^-^ ")

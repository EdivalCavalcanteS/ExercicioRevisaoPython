print ("Digite sua primeira nota (Ex; 0.0 ,5.5 ,10.0)")
nota1 = float(input())

print ("Digite sua segunda nota (Ex; 0.0 ,5.5 ,10.0)")
nota2 = float(input())

print ("Digite sua terceira nota (Ex; 0.0 ,5.5 ,10.0)")
nota3 = float(input())

media = (nota1 + nota2 + nota3) / 3

if media == 10:
   print("Aprovado com Distinção")
   print("media alcançada = %d"%(media))


elif media >= 7:
   print("aprovado")
   print("media alcançada = %d"%(media))


else:
   print("reprovado")
   print("media alcançada = %d"%(media))

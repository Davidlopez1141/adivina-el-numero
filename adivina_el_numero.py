from random  import *

from more_itertools import numeric_range 

# entrada 

x = int(input("ingrese un numero del 0 al 50:"))
# proceso 
numero generado = randint(0, 50) 
if x == numero generado : 
    print("el numero",str(x),"es igua a", str(numero_generado))
elif x < numero generado:
    print("el numero",str(X),"es menor a",str(numero_generado))
else:
     print("el numero",str(x),"es mayor a",str(numero_generado))
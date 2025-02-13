# Quiz instrucciones condicionales
"""Dados tres números a, b y c, correspondientes a la longitud de los lados de una figura geométrica, determinar si pueden formar los lados de un triángulo."""

print("------------------------------")
print("----- VERIFICAR TRIANGULO ----")
print("------------------------------")


# input
a = float(input("Ingrese el valor de a: "))     
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

# processing
if a + b > c:
    print(" si se puede formar un triangulo")
elif a + b < c :
    print("no se puede formar un triangulo")
elif a + c > b:
     print(" si se puede formar un triangulo")
elif a + c < b:
    print("no se puede formar un triangulo")
else:
    print("no se puede formar un triangulo")
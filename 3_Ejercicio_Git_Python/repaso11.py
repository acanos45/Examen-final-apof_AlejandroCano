nombre = input ("Como te llamas?")
veces = int(input ("Cuantas veces quieres que te salude"))

for i in range(veces):
    print(" Hola " + nombre , end="")
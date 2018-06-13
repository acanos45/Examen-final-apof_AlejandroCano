cont = 0
palabra = input ("Dime una palabra:")
for letra in palabra:
    print("La letra ahora es: " + letra)
    if letra == "a" or letra == "A":
            cont = cont + 1
print ("El numero de letras a que aparecen en la palabra són:")
print(str(cont))
#strin es una cadenas de texto
myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))

#esto se usa para juntar cadenas con el simbolo +
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

#el comando input se usa para que el usuario escriba algo 
#el codigo no continua si el usuario no escribe 
name = input("What is your name? ")
print(name)

#el siguiente comando es para usar las cadenas de salida 
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like a {} {}!".format(name,color,animal))
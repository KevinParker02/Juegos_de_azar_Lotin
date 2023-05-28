import random

#Desarrolladores Anto, Ricardo y Kevin :)

print("\n¡Bienvenido a Lotín!");
print("\nIngrese sus 5 números de la suerte, recuerde que deben ser número entre el 1 y el 49")
lista=[]; #Esta lista almacenará los valores que ingresaremos más adelante.
cont=0; #Cuenta los intentos, la idea es que no cuente los erroneos.

while cont<5:
    try:
        nums=int(input("\nIngrese un número: "));
        if nums>=1 and nums<=49: #Condición
            lista.append(nums); #Agregará los números ingresados a la lista.
            cont+=1; #Aumentará a medida que el usuario ingrese un valor dentro del rango, sino, lo repetirá hasta que se complete los 5 números.
        else:
            print("\nSolo debe ingresar un valor númerico entre el 1 y el 49.");
    except ValueError:
        print("\nSolo se deben ingresar valores númericos.");
print(f"\nUsted ingresó los siguientes números: {lista}");

print("\nLos número sorteados en la ronde 1 fueron: \n");
lista_b=list(range(1,49,1)); #Rango de la lista donde se sacarán los número aleatorios.
lista_c=[]; #Será la lista que guardará los nuevos números.
for n in range(1,6,1): #Las veces que se reperirá el random.
    ram_num=random.choice(lista_b); #.choice es una función del random que selecionará el número.
    lista_c.append(ram_num); #Agregará cada número a la lista.
    print(ram_num); #Impime cada valor aleatorio.

if lista==lista_c:
    print("¡Ganó socio!");
else:
    print("\nNo ganó socio.");


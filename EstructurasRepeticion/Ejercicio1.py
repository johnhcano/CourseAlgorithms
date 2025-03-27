n = 0
total = 0
numero = 0
suma = 0

#pedir n (cantidad de números) por teclado
total = int(input("Cantidad de números:"))
while(total > 0):
    numero = int(input("Digite un número:"))
    suma += numero # suma = suma + numero
    total -= 1 #total = total - 1
    n+=1

#forma_1
print("1. La suma de los " , str(n) , " números es: " , str(suma))
#forma_2
print(f"2. La suma de los {n} números es: {suma}")
#Condicinal dentro del format
print(f"La suma es: {suma} -> {'Par' if suma%2 == 0 else 'Impar'}")
#forma_3
print("3. La suma de los {} números es: {}".format(n,suma))

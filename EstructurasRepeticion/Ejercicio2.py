'''
Diseñar una función que calcule x^n para x, variable real y n variable entera.

2^4 => 2 * 2 * 2 * 2
x^n => x * ..... * x
'''
x = int(input("Digite x"))
n = int(input("Digite n"))
resultado = 1
i = 1
while(i <= n):
    resultado *= x #resultado = resultado * x
    i += 1

print(f"{x} elevado a la {n} => {resultado}")


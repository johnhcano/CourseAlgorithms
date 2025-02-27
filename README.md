# CourseAlgorithms

Clase 1
Clase 2
Clase 3 Expresiones

Clase 4 Condicionales

Operaciones Lógicas

AND - && - ^ - y
V V -> V
V F -> F
F V -> F
F F -> F

OR - || - v - o
V V -> V
V F -> V
F V -> V
F F -> F

¬ - Negación - !
V -> F
F -> V

Ejemplos:
A <- 4
B <- 10
C <- 5
(A >= B) && (B <= C) R// (F && F) -> F
(A <= B) && (B <= C) R// (V && F) -> F
(A <= B) || (B <= C) R// (V || F) -> V
(A >= B)! && (B <= C)! R// (V && V) -> V 


Ejecicios Libro Fundamentos de Programación de Luis Joyanes Aguilar Pag Libro->155 PDF->185
4.1 al 4.10 Pseudocodigo + Diagrama de flujo 

4.1 a
Algoritmo Angulo_90_grados
var
    Entero: angulo
inicio
    leer angulo
    angulo <- 70
    si angulo == 90 entonces
        mostrar "El ángulo es un ángulo recto"
    si_no
        mostrar "El ángulo no es un ángulo recto"
    fin_si 
fin    

![image](https://github.com/user-attachments/assets/0dca524f-856c-4592-aa59-da05eab972ed)


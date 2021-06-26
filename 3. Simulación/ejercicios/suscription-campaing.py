"""Ejercicio 5.4
Se desea saber el resultado economico de una campaña de suscripción
 puerta a puerta; para ello se realiza un estudio de simulación en
 base a información muestral obtenida de campañas anteriores.
 El nº máximo de suscripciones que puede hacer una persona que es
 visitada por el vendedor es de 4, pero la probabilidad varía si
 es hombre o mujer. La distribución de probabilidad del nº de
 suscripciones según el sexo del comprador es el siguiente:

Mujeres
N Articulos    1     2     3    4
Probabilidad  0.6   0.3   0.1   0

Hombres
N Articulos    1     2     3    4
Probabilidad  0.1   0.4   0.3  0.2

Cuando el vendedor/a visita a los clientes establecidos, en un 70%
de los casos no hay nadie o no son recibidos. Cuando son recibidos,
un 80% de las veces abre un hombre y un 20% una mujer.
Cuando abre un hombre un 25% de las veces se consigue la venta,
pero este porcentaje es sólo el 15% si abre una mujer.
El beneficio por suscripción vendida es de 3.000 pts.
Determinar el beneficio total de la campaña simulando 15 visitas.

Números Aleatorios:
2, 7, 45, 4, 9, 2, 9, 47, 5, 5, 3, 4, 8, 9, 4, 8, 9, 0, 4, 8, 9, 7, 5, 8, 3, 4, 9, 8,
7, 4, 5, 8, 5, 3, 8, 2, 2, 47, 8, 9, 4, 7, 8, 9, 8, 8, 1, 3, 26, 5, 9, 8, 8, 9, 5, 6,
7, 7, 8, 5, 6, 3, 1, 0, 10, 2, 3, 4, 8, 5, 7, 2, 3, 36, 4, 5, 4, 7, 5, 0, 9, 28, 2, 7,
31, 0, 9, 29, 3
"""

from random import randint

random = [2, 7, 45, 4, 9, 2, 9, 47, 5, 5, 3, 4, 8, 9, 4, 8, 9, 0, 4, 8, 9, 7, 5, 8, 3, 4, 9, 8, 7, 4, 5, 8, 5, 3, 8, 2, 2,
          47, 8, 9, 4, 7, 8, 9, 8, 8, 1, 3, 26, 5, 9, 8, 8, 9, 5, 6, 7, 7, 8, 5, 6, 3, 1, 0, 10, 2, 3, 4, 8, 5, 7, 2, 3, 36, 4, 5, 4, 7, 5, 0, 9, 28, 2,
          7, 31, 0, 9, 29, 3]

index = 0
profit = 0

for i in range(15):
    if randint(1, 100) < 30:                                           # Hay gente en casa

        if randint(1, 100) < 80:                                       # Abre un hombre

            if randint(1, 100) <= 25:                                  # Se consigue la venta

                if randint(1, 100) <= 10:                              # Vende un Articulo
                    profit += 3000
                elif randint(1, 100) > 10 and randint(1, 100) <= 40:   # Vende dos articulos
                    profit += 3000 * 2
                elif randint(1, 100) > 40 and randint(1, 100) <= 70:   # Vende tres articulos
                    profit += 3000 * 3
                else:                                                  # Vende cuatro articulos
                    profit += 4000

        else:                                                          # Abre una mujer
            if randint(1, 100) <= 15:                                  # Se consigue la venta

                if randint(1, 100) <= 60:                              # Vende un Articulo
                    profit += 3000
                elif randint(1, 100) > 60 and randint(1, 100) <= 90:   # Vende dos articulos
                    profit += 3000 * 2
                elif randint(1, 100) > 90 and randint(1, 100) <= 100:  # Vende tres articulos
                    profit += 3000 * 3
                else:                                                  # Vende cuatro articulos
                    profit += 4000

print(profit)

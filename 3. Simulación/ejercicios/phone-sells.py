""" Ejercicio 5.5
Una empresa quiere introducirse en la venta por teléfono, pero desea determinar cuáles
son los ingresos medios que supone esta nueva estrategia de ventas por teléfono con el
fin de determinar los futuros beneficios. Se sabe de estudios de otras empresas dedicadas
a lo mismo, que:

¸ De las llamadas realizadas, el 55% de las llamadas contestan y aceptan, el 25%
contestan y no aceptan y el resto no contestan (no hay nadie en casa, contestador,
teléfono erróneo,...).

¸ Las ventas difieren de si es un hombre o una mujer quien contesta.

¸ La probabilidad de que sea una mujer es del 55%.

¸ Las probabilidades de ventas están definidas de la siguiente manera:

Mujeres
N Articulos     0     1       2      3      4     5
Probabilidad  0.04   0.16   0.30   0.25   0.20   0.05

Hombres
N Articulos     0     1       2      3      4     5
Probabilidad  0.15   0.10   0.15   0.30   0.20   0.10

El precio medio del artículo es de 3000 pts, simule un día laboral donde pueden realizarse unas 20
llamadas.
Números aleatorios:
39, 27, 79, 17, 98, 62, 28, 75, 34, 43, 84, 14, 32, 70, 90, 26, 74, 17, 59, 12, 23, 63, 80, 65, 44, 89, 79,
82, 01, 18, 86, 55, 59, 26, 96, 31, 74, 54, 90, 95, 61, 62
"""

numbers = [39, 27, 79, 17, 98, 62, 28, 75, 34, 43, 84, 14,
           32, 70, 90, 26, 74, 17, 59, 12, 23, 63, 80, 65, 44, 89, 79,
           82, 0, 18, 86, 55, 59, 26, 96, 31, 74, 54, 90, 95, 61, 62]  # 42
index = 0

def run():
    earnings = 0
    index = 0
    if numbers[index] <= 55:  # Contesta y Acepta
        index+=1
        if numbers[index] <= 55:  # Contesta Mujer
            index+=1
            if numbers[index] <= 4:  # 0 articulos
                index+=1
            elif numbers[index] > 4 and numbers[index] <= 20:  # 1 Articulo
                index+=1
                earnings += 3000
            elif numbers[index] > 20 and numbers[index] <= 50:  # 2 Articulos
                index+=1
                earnings += 3000*2
            elif numbers[index] > 50 and numbers[index] <= 75:  # 3 Articulos
                index+=1
                earnings += 3000*3
            elif numbers[index] > 75 and numbers[index] <= 95:  # 4 Articulos
                index+=1
                earnings += 3000*4
            else:  # 5 Articulos
                index+=1
                earnings += 3000*5

        else:  # Contesta hombre
            if numbers[index] <= 15: # 0 Articulos
                index+=1

            elif numbers[index] > 15 and numbers[index] <= 25: # 1 Articulos
                index+=1
                earnings += 3000
            elif numbers[index] > 25 and numbers[index] <= 40: # 2 Articulos
                index+=1
                earnings += 3000*2
            elif numbers[index] > 40 and numbers[index] <= 70: # 3 Articulos
                index+=1
                earnings += 3000*3
            elif numbers[index] > 70 and numbers[index] <= 90: # 4 Articulos
                index+=1
                earnings += 3000*4
            else:
                index+=1
                earnings += 3000*5

    elif numbers[index] > 55 and numbers[index] <= 80:  # Contesta y no aceptan
        index+=1
    else:  # No contestan
        index+=1

    print(earnings)


if __name__ == "__main__":
    run()
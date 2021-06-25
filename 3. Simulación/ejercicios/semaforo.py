"""
Utilice los números aleatorios de un dígito, 5, 2, 4, 9, 7,
para generar observaciones aleatorias para El color de la luz
del semáforo que llega al azar, si el 40% del tiempo está en verde, 10%
en amarillo y 50% en rojo.
"""


def run():
    numbers = [5, 2, 4, 9, 7]
    for number in numbers:
        if number <= 4:
            print(f"{number}. Verde")
        elif number == 5:
            print(f"{number}. Amarillo")
        else:
            print(f"{number}. Rojo")


if __name__ == "__main__":
    run()

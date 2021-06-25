"""
Utilice los números aleatorios de un dígito, 5, 2, 4, 9, 7,
para generar observaciones aleatorias para la tirada al aire de una moneda
"""


def run():

    flips = [5, 2, 4, 9, 7]

    for flip in flips:
        if flip < 5:
            print(f"{flip} \t\t\t Cara")
        else:
            print(f"{flip} \t\t\t Cruz")


if __name__ == "__main__":
    run()

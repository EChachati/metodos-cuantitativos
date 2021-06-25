"""
Utilice el método congruencial mixto para generar las siguientes sucesiones de nº
aleatorios.
    a) Una sucesión de 10 n.a. enteros de un dígito tal que
     Xn+1  = (Xn + 3)(modulo10) y X0 = 2

    b) Una sucesión de 8 n.a. enteros entre 0 y 7 de un dígito
     tal que 5( )(1 )8 X 1 X módulo n + = n + y X0=1.

    c) Una sucesión de 5 n.a. enteros de un dígito tal que
    61( )(27 100) X 1 X módulo n + = n + y X0=100.
"""

"""
Un generador lineal congruencial (GLC) es un algoritmo que permite
 obtener una secuencia de números pseudoaleatorios calculados con
 una función lineal definida a trozos discontinua. Es uno de los
 métodos más antiguos y conocidos para la generación de números
 pseudoaleatorios.
"""

"""
Método Congruencial Mixto o Lineal: los generadores congruenciales
lineales generan una secuencia de números pseudoaleatorios en la cual el
próximo número pseudoaleatorio es determinado a partir del último número
generado, es decir, el número pseudoaleatorio Xn+1 es derivado a partir del
número pseudoaleatorio Xn La relación de recurrencia para el generador
congruencial mixto es Xn+1 =(a Xn+c) mod m, en donde
• X0 = es la semilla
• a = el multiplicador
• c = constante aditiva
• m = el modulo (m > X0, a,c)
• X0, a, c > 0
"""


class MixedCongruentialGenerator:

    def __init__(self, multiplicator, aditive_constant, seed,  module):
        self.seed = seed
        self.multiplicator = multiplicator
        self.aditive_constant = aditive_constant
        self.module = module

    def get_random_number(self, length=1):

        result = []

        for i in range(length):
            number = (self.multiplicator * self.seed +
                      self.aditive_constant) % self.module
            number_munoz = number / self.module
            result.append((number, number_munoz))
            self.seed = number

        return result


if __name__ == "__main__":
    generator = MixedCongruentialGenerator(5, 7, 4, 8)

    print("----- Guide Example -----")
    numbers = generator.get_random_number(10)
    for number in numbers:
        print(f"{number[0]} ({number[1]})")

    print("----- Exercise A -----")

    generator_A = MixedCongruentialGenerator(
        multiplicator=1, aditive_constant=3, seed=2, module=10
    )
    
    numbers = generator_A.get_random_number(10)
    for number in numbers:
        print(f"{number[0]} ({number[1]})")

    print("----- Exercise B -----")

    generator_B = MixedCongruentialGenerator(
        multiplicator=5, aditive_constant=1, seed=1, module=8
    )

    numbers = generator_B.get_random_number(8)
    for number in numbers:
        print(f"{number[0]} ({number[1]})")

    print("----- Exercise C -----")

    generator_C = MixedCongruentialGenerator(
        multiplicator=61, aditive_constant=27, seed=100, module=100
    )

    numbers = generator_C.get_random_number(5)
    for number in numbers:
        print(f"{number[0]} ({number[1]})")

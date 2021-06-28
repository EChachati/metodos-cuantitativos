# Simulation For M/M/1 Systems

from math import e, factorial
from random import randint


class MM1:
    def __init__(self, clients, capacity):
        """
        - clients = λ = Número medio de llegadas por unidad de tiempo
        - capacity = µ = Numero medio de paquetes que el servidor puede atender por unidad de tiempo
        - AverageTimeInSystem = W
        """
        self.__lambda = clients
        self.__mu = capacity
        self.__ws = 1 / (capacity - clients)
        self.__wq = self.__ws - (1/self.__mu)
        self.__p = self.__lambda / self.__mu
        self.__ls = self.__lambda * self.__ws
        self.__lq = self.__lambda * self.__wq
        self.__p0 = (1 - self.__p)

        self.current_clients = 0
        self.total_clients = 0

    def probabilities_n_packeges_in_queue(self, n: int):
        """Probabilidad de que haya N clientes en la cola"""
        return (self.__p**n)(1 - self__p)

    def probabilities_wait_t_time(self, t: int):
        """Probabilidad que un cliente deba esperar T tiempo en sistema"""
        return e ** (-self.__mu(1 - self__p)*t)

    def probabilities_n_clients_arrives_in_t_time(self, n: int, t: int = 1):
        """Probabilidad que lleguen N clientes en T tiempo"""
        return e ** (-self.__lambda*t) * ((self.__lambda*t)**n)/factorial(n)

    def get_probabilities_to_n_clients(self, n):
        """Probabilidad de que lleguen clientes de 0 clientes a N clientes"""
        return [self.probabilities_n_clients_arrives_in_t_time(i) for i in range(n+1)]

    def get_accumulated_probabilities_to_n_clients(self, n):
        """Probabilidad de que lleguen clientes de 0 clientes a N clientes de forma acumulativa"""
        prev = 0
        probabilities = []
        for i in range(n+1):
            actual = self.probabilities_n_clients_arrives_in_t_time(i) + prev
            prev = actual
            probabilities.append(actual)
        return probabilities

    def __str__(self):
        return f"""
        Número medio de llegadas por unidad de tiempo = λ = {self.__lambda}
        Numero medio de paquetes que el servidor puede atender por unidad de tiempo = µ = {self.__mu}
        Tiempo Medio que permanece un paquete en sistema = Ws = {self.__ws}
        Tiempo medio de espera en la cola = Wq = {self.__wq}
        Intensidad de Trafico en el Sistema = p = {self.__p}
        Número medio de paquetes en Sistema = Ls = {self.__ls}
        Número medio de paquetes en Cola = Lq = {self.__lq}
        Probabilidad de que no haya paquetes en sistema = P0 = {self.__p0}
        """


def initialize(clients_per_minute, capacity_per_minute):

    # clients_per_minute = 0.75
    # capacity_per_minute = 1

    QUEUE = MM1(clients_per_minute, capacity_per_minute)

    probabilities = (QUEUE.get_accumulated_probabilities_to_n_clients(4))
    print(f"""Probabilidades de que Lleguen N clientes en un minuto:""")
    for i, probabilitie in enumerate(QUEUE.get_probabilities_to_n_clients(4)):
        print(f"Llegan {i} clientes: {round(probabilitie*100,2)} %")

    print(
        f"Llegan {len(probabilities)} clientes: {round(100 - probabilities[len(probabilities)-1]*100,2)} %")
    print()

    probabilities = [int(probabilitie*100000)
                     for probabilitie in probabilities]

    return {
        "queue": QUEUE,
        "probabilities": probabilities
    }


def simulation(clients_per_minute, capacity_per_minute, time: int = 60):
    """
    Suponga que en una estación con un solo servidor llegan en promedio 0.75 clientes
    por minuto, Se tiene capacidad para atender en promedio a 1 clientes por minuto.

    Modelo orientado a los eventos: Verifica la cantidad de clientes que pueden estar
    en la cola y cuantos pueden entrar cada minuto a lo largo de una hora

    Simulación Orientada a los intervalos: el reloj de simulación es avanzado a
    incrementos de tiempos fijos
    """

    initialized_data = initialize(clients_per_minute, capacity_per_minute)
    QUEUE = initialized_data["queue"]
    probabilities = initialized_data["probabilities"]

    for minute in range(time+1):  # Rutina de Tiempo
        print(
            f"\n----------------------------------------- Minuto {minute} -----------------------------------------")
        random_number = randint(1, 100000)
        # Inicio rutina de Evento

        if QUEUE.current_clients > 0:
            print("\t\t\t\t Ha salido un cliente")
            QUEUE.current_clients -= 1

        for i, probabilitie in enumerate(probabilities):
            if i == 0 and random_number < probabilitie:
                print(
                    f"Numero Aleatorio: {random_number}\t\t No Entro ningún cliente nuevo \t\tClientes Actuales: {QUEUE.current_clients}")
                break
            elif random_number <= probabilitie and random_number > probabilities[i-1]:
                QUEUE.current_clients += i
                QUEUE.total_clients += i
                print(
                    f"Numero Aleatorio: {random_number}\t\t Entró {i} cliente(s) nuevo(s) \t\tClientes Actuales: {QUEUE.current_clients}")
                break
            elif random_number > probabilities[len(probabilities)-1]:
                QUEUE.current_clients += len(probabilities)
                QUEUE.total_clients += len(probabilities)
                print(
                    f"Numero Aleatorio: {random_number}\t\t Entró {len(probabilities)} clientes nuevos \t\tClientes Actuales: {QUEUE.current_clients}")
                break

        # Fin rutina de Evento

    # Informe
    print(f"""

---------------------------------------------------------------------------------------------
--------------------------------------- Informe Final ---------------------------------------
---------------------------------------------------------------------------------------------

    Clientes Actuales tras una hora:                {QUEUE.current_clients} Clientes
    Clientes Totales en una hora:                   {QUEUE.total_clients} Clientes

    INFORMACIÓN DE LA COLA:

    {QUEUE}

---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
    """)

    return QUEUE


def run():
    print()
    clients_per_minute = 0.75
    capacity_per_minute = 1
    simulation(clients_per_minute, capacity_per_minute, time=60)


if __name__ == '__main__':
    run()

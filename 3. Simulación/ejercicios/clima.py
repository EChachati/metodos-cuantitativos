""" Ejercicio 5.3
El clima se puede considerar un sistema estocástico, porque evoluciona de una
manera probabilística de un día a otro. Suponga que para cierto lugar este
comportamiento probabilístico satisface la siguiente descripción:
La probabilidad de un día despejado para mañana si hoy no llueve es del 80% y
la probabilidad de un día despejado para mañana si hoy llueve es del 40%.

Nª aleatorios: 8-1-3-7-2-7-1-6-5-5
"""
rained = True

probabilities = [8, 1, 3, 7, 2, 7, 1, 6, 5, 5]
days = [rained]

for probabilitie in probabilities:
    if rained:
        if probabilitie <= 40:
            rained = False
    else:  # Not rained
        if probabilitie <= 20:
            rained = True

    days.append(rained)

for i, e in enumerate(days):
    print(f"Day {i} did rain? -> {e}")

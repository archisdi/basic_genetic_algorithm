import math
import numpy as np
import random


def initialization(n):
    return np.random.randint(10, size=n * 2)


def decode_each(ra, rb, k, n):
    N = 0
    for i in range(1, n + 1):
        N = N + (9 * (math.pow(10, -i)))

    res = 0
    for i in range(1, n + 1):
        res = res + (k[i - 1] * (math.pow(10, -i)))

    return rb + ((ra - rb) / N) * res


def decode(kromosom, ra, rb, n):
    kromosom = np.split(kromosom, 2)
    k = []
    k.append(decode_each(ra, rb, kromosom[0], n))
    k.append(decode_each(ra, rb, kromosom[1], n))
    return k


def fitness(x1, x2):
    a = 0.00001
    h = (4 - (2.1 * math.pow(x1, 2)) + (math.pow(x1, 4)) / 3) * math.pow(x1, 2) + (x1 * x2) + (-4 + (
        4 * math.pow(x2, 2))) * math.pow(x2, 2)

    return 1 / h + a


def sigma_scaling(population):
    c = 2
    sum = np.average(population)
    sd = np.std(population)
    for i in range(0, len(population)):
        population[i] = population[i] + (sum - c * sd)
        if (population[i] < 0):
            population[i] = 0

    return population


def parent_selection(population):
    max = np.sum(population)
    pick = random.uniform(0, max)
    current = 0
    for value in population:
        current += value
        if current > pick:
            return population.index(value)


def recombination(population, rp):
    new_pop = []
    pick = random.uniform(0, 1)
    for i in range(0, len(population), 2):
        if (pick <= rp):
            p1 = np.split(population[i], 2)
            p2 = np.split(population[i + 1], 2)
            new_pop.append(np.concatenate((p1[0], p2[1])))
            new_pop.append(np.concatenate((p2[0], p1[1])))
        else:
            new_pop.append(population[i])
            new_pop.append(population[i+1])

    return new_pop


def mutation(population, mp):
    new_pop = []
    for i in range(0, len(population)):
        pick = random.uniform(0, 1)
        if (pick <= mp):
            index = np.random.randint(0, len(population[i])-1)
            new_val = np.random.randint(0, 10)
            while (new_val == population[i][index]):
                new_val = np.random.randint(0, 10)
            population[i][index] = new_val
            new_pop.append(population[i])
        else:
            new_pop.append(population[i])

    return new_pop
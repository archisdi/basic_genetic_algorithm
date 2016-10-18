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


def cost(x1, x2):
    h = (4 - (2.1 * math.pow(x1, 2)) + (math.pow(x1, 4)) / 3) * math.pow(x1, 2) + (x1 * x2) + (-4 + (
        4 * math.pow(x2, 2))) * math.pow(x2, 2)

    return h


def fitness(population, ra, rb, n):
    fitness = []
    for data in population:
        x = decode(data, ra, rb, n)
        fitness.append(1 / (cost(x[0], x[1]) + abs(rb)))

    return fitness


def roulette_wheel(population, fitness_val):
    max = np.sum(fitness_val)

    pick = random.uniform(0, max)
    current = 0
    for value in fitness_val:
        current += value
        if current > pick:
            return (population[fitness_val.index(value)])


def linear_ranking(population, fitness_val):
    population = np.array(population)
    fitness_val = np.array(fitness_val)
    inds = fitness_val.argsort()
    sortedFitness = sorted(inds)
    sortedPopulation = population[inds]

    return sortedPopulation, sortedFitness


def parent_selection(population, fitness_val, ra, rb, n):
    new_pop = []
    new_pop.append(population[0])
    new_pop.append(population[1])

    # Linear Ranking
    population, fitness_val = linear_ranking(population, fitness_val)

    for i in range(2, len(population)):
        chs = roulette_wheel(population, fitness_val)
        new_pop.append(chs)

    return new_pop


def recombination(population, rp):
    def split_list(list, point):
        return list[:point], list[point:]

    new_pop = []
    new_pop.append(population[0])
    new_pop.append(population[1])

    for i in range(2, len(population), 2):
        rand = random.uniform(0, 1)
        if (rand < rp):
            point = random.randint(1, len(population[i]) - 1)
            p1 = split_list(population[i], point)
            p2 = split_list(population[i + 1], point)
            new_pop.append(np.concatenate((p1[0], p2[1])))
            new_pop.append(np.concatenate((p2[0], p1[1])))
        else:
            new_pop.append(population[i])
            new_pop.append(population[i + 1])

    return new_pop


def mutation(population,mp):
    new_pop = []
    new_pop.append(population[0])
    new_pop.append(population[1])

    rand = random.uniform(0, 1)

    for i in range(2, len(population)):
        if (rand < mp):
            index = np.random.randint(0, 5)
            new_val = np.random.randint(0, 10)

            while (new_val == population[i][index]):
                new_val = np.random.randint(0, 10)

            population[i][index] = new_val
            new_pop.append(population[i])
        else:
            new_pop.append(population[i])

    return new_pop
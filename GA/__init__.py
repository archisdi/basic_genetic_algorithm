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

def cost(x1,x2):
    h = (4 - (2.1 * math.pow(x1, 2)) + (math.pow(x1, 4)) / 3) * math.pow(x1, 2) + (x1 * x2) + (-4 + (
        4 * math.pow(x2, 2))) * math.pow(x2, 2)

    return  h

def fitness(population, ra, rb, n):
    a = 0.00001
    fitness = []
    for data in population:
        x = decode(data, ra, rb, n)
        fitness.append(1/cost(x[0],x[1]) + a)

    return fitness

def filter_fitness(fitess_val):
    for i in range(0,len(fitess_val)):
        if (fitess_val[i] < 0):
            fitess_val[i] = 0
    return fitess_val

def window_scaling(fitness,min):
    scaled_fitness = []
    for data in fitness:
        scaled_fitness.append(data-min)
    return scaled_fitness

def roulette_wheel(population, fitness_val,ra, rb, n, min):
    fitness_val = filter_fitness(fitness_val)
    fitness_val = window_scaling(fitness_val,min)
    new_pop = []
    new_pop.append(population[0])
    new_pop.append(population[1])
    max = np.sum(fitness_val)

    def choose(fitness_val):
        pick = random.uniform(0, max)
        current = 0
        for value in fitness_val:
            current += value
            if current > pick:
                return (population[fitness_val.index(value)])

    for i in range(2, len(population)):
        chs = choose(fitness_val)
        if( i > 0 ):
            if(i % 2 != 0):
                x1 = decode(new_pop[i-1],ra,rb,n)
                a1 = 1/cost(x1[0],x1[1])+0.0001
                x2 = decode(chs,ra,rb,n)
                a2 = 1/cost(x2[0],x2[1])+0.0001

                while(a1 == a2):
                    chs = choose(fitness_val)
                    x2 = decode(chs, ra, rb, n)
                    a2 = 1/cost(x2[0], x2[1])+0.0001
        new_pop.append(chs)

    return new_pop



def recombination(population, rp):
    new_pop = []
    new_pop.append(population[0])
    new_pop.append(population[1])
    for i in range(2, len(population), 2):
        pick = random.uniform(0, 1)
        if (pick < rp):
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
    new_pop.append(population[0])
    new_pop.append(population[1])
    for i in range(2, len(population)):
        pick = random.uniform(0, 1)
        if (pick < mp):
            index = np.random.randint(0, 5)
            new_val = np.random.randint(0, 10)
            while (new_val == population[i][index]):
                 new_val = np.random.randint(0, 10)
            population[i][index] = new_val
            new_pop.append(population[i])
        else:
            new_pop.append(population[i])

    return new_pop


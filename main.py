import GA
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ra  = 3    # Batas atas
rb  = -3   # Batas bawah
n   = 5    # Panjang reptesentasi variable
pop = 100  # Total individu tiap populasi
rp  = 0.8  # Probabilitas rekombinasi
mp  = 0.1  # Probabilitas mutasi
g   = 200  # Generasi

kromax = []     # kromosom terbaik
fitmax = []     # fitness kromosom terbaik
population = [] # populasi

# initialization
for i in range(0, pop):
    population.append(GA.initialization(n))

# main iteration
for i in range(0, g):
    # fitness calculation
    fitAwal = []
    fitAwal = GA.fitness(population, ra, rb, n)

    # parent selection
    gen = []
    gen = GA.parent_selection(population, fitAwal, ra, rb, n)

    # recombination
    offsprings = []
    offsprings = GA.recombination(gen,rp)

    # mutation
    mutated = []
    mutated = GA.mutation(offsprings,mp)

    # generational replacement
    population = mutated
    fit = []
    fit = GA.fitness(population, ra, rb, n)

    # elitism
    max = np.amax(fit)
    index = fit.index(max)
    population[0] = population[index]
    population[1] = population[index]

    # best chromosome records
    kromax.append(population[index])
    fitmax.append(max)

# plot animation
x = np.arange(0, g)
y = fitmax
bestC = (1 / fitmax[-1]) - 2
bestK = GA.decode(kromax[-1],ra,rb,n)

fig, ax = plt.subplots()
line, = ax.plot(x, y, color='g')

def update(num, x, y, line):
    line.set_data(x[:num], y[:num])
    return line,

ani = animation.FuncAnimation(fig, update, len(x), fargs=[x, y, line],
                              interval=0.001, blit=True, repeat=False)
plt.ylabel('Fitness')
plt.xlabel('Generasi')
ax.text(0.95, 0.035, ('f(x1,x2) : ',bestC),
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='black', fontsize=10, style='italic',
        bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})

ax.text(0.95, 0.15, ('x1:',bestK[0],'x2:',bestK[1]),
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='black', fontsize=10, style='italic',
        bbox={'facecolor':'green', 'alpha':0.5, 'pad':10})
print(bestK[0],bestK[1])
plt.show()
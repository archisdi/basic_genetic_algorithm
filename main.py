import GA
import numpy as np

ra = 3  # Batas atas
rb = -3  # Batas bawah
n = 3  # panjang reptesentasi variable
pop = 10  # Total individu tiap populasi
rp = 0.8  # Probabilitas rekombinasi
mp = 0.1  # Probabilitas mutasi
g = 1000  # iterasi

kromax = []
fitmax = []
popAwal = []
minfit = 0

for i in range(0, pop):
    popAwal.append(GA.initialization(n))


for i in range(0, g):
    #hitung fitness
    fitAwal = []
    fitAwal = GA.fitness(popAwal,ra,rb,n)

    # seleksi orangtua
    gen = []
    gen = GA.roulette_wheel(popAwal, fitAwal, ra, rb, n,minfit)
    #print(gen)

    # rekombinasi
    new_gen = []
    new_gen = GA.recombination(gen, rp)

    # mutation
    mutate = []
    mutate = GA.mutation(new_gen, mp)

    popAwal = mutate
    fit = []
    fit = GA.fitness(popAwal,ra,rb,n)

    index = fit.index(np.amin(fit))
    min_krom = GA.decode(popAwal[index],ra,rb,n)

    minfit = 1/GA.cost(min_krom[0],min_krom[1])+0.0001
    if(minfit < 0):
        minfit = 0
    print(minfit)

    index = fit.index(np.amax(fit))
    popAwal[0] = popAwal[index]
    temp = popAwal[index]
    popAwal[index] = popAwal[1]
    popAwal[1] = temp
    print('Gen ',i+1,' : ',fit[index],' - ',popAwal[index],' - ',index)
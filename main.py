import GA
import numpy as np

ra = 3  # Batas atas
rb = -3  # Batas bawah
n = 5  # panjang reptesentasi variable
pop = 10  # Total individu tiap populasi
rp = 0.8  # Probabilitas rekombinasi
mp = 0.1  # Probabilitas mutasi
g = 10000  # iterasi

kromax = []
fitmax = []
popAwal = []

for i in range(0, pop):
    popAwal.append(GA.initialization(n))


for i in range(0, g):
    #hitung fitness
    fitAwal = []
    fitAwal = GA.fitness(popAwal,ra,rb,n)

    # seleksi orangtua
    gen = []
    gen = GA.parent_selection(popAwal, fitAwal, ra, rb, n)

    # rekombinasi
    new_gen = []
    new_gen = GA.recombination(gen, rp)

    # mutation
    mutate = []
    mutate = GA.mutation(new_gen, mp)

    #Generasi Baru
    popAwal = mutate
    fit = []
    fit = GA.fitness(popAwal,ra,rb,n)

    index = fit.index(np.amax(fit))
    popAwal[0] = popAwal[index]
    popAwal[1] = popAwal[index]
    # print('----------------------------------------------------------------------------------------------------')
    print('Gen ',i+1,' : ',fit[index],' - ',popAwal[index],' - ',index)
    # print(popAwal)
    # print('----------------------------------------------------------------------------------------------------')
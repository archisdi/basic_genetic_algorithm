import GA

ra = 3      #Batas atas
rb = -3     #Batas bawah
n = 3       #panjang reptesentasi variable
pop = 10    #Total individu tiap populasi
rp = 0.8    #Probabilitas rekombinasi
mp = 0.1    #Probabilitas mutasi

#inisialisasi generasi pertama
popAwal = []
for i in range(0,pop):
    popAwal.append(GA.initialization(n))

#menentukan fitness dari generasi pertama
fitAwal = []
for i in range(0,pop):
    k = GA.decode(popAwal[i],ra,rb,n)
    fitAwal.append(GA.fitness(k[0],k[1]))


#seleksi orangtua
gen = []
for i in range(0,pop):
    gen.append(popAwal[GA.parent_selection(fitAwal)])

#rekombinasi
new_gen = []
new_gen = GA.recombination(gen,rp)

#mutation
mutate = []
mutate = GA.mutation(new_gen,mp)

print(popAwal)
print(gen)
print(new_gen)
print(mutate)

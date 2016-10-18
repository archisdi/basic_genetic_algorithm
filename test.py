import GA
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ra = 3  # Batas atas
rb = -3  # Batas bawah
n = 5  # Panjang reptesentasi variable
pop = 50  # Total individu tiap populasi
rp = 0.8  # Probabilitas rekombinasi
mp = 0.1  # Probabilitas mutasi
g = 1000  # Generasi

def real_rep(ra,rb,x):
    return (rb) + (ra - rb) * x

x = real_rep(ra,rb,0.4855594460293093)
y = real_rep(ra,rb,0.6201771207122992)

cost = (GA.cost(-0.0821708217082,0.652716527165))

fitness = 1 / (cost + 3)

print(cost)
print(fitness)
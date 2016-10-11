import GA
import numpy as np

k1 = np.random.randint(10, size=6)
k2 = np.random.randint(10, size=6)
k = []
k.append(k1)
k.append(k2)
print(k1)

GA.mutation(k,0.1)

print(k1)
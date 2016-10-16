import GA
import numpy as np

ra = 3      #Batas atas
rb = -3     #Batas bawah
n = 5       #panjang reptesentasi variable

# array([8, 1, 9, 9, 2, 3])
test= [4, 5, 3, 5, 3, 9]
#8 0 5 4 4 3 6 0 8 1
# x1 = GA.decode_each(ra,rb,[8, 0, 5, 4, 4],n)

x = np.linspace(0, 10, 100)
y = np.sin(x)

print('test',(1))
import math

def cost(x1,x2):
    return (4-(2.1*math.pow(x1,2))+(math.pow(x1,4))/3) * math.pow(x1,2) + (x1*x2) + (-4+(4*math.pow(x2,2))) * math.pow(x2,2)

print(cost(-3,2))
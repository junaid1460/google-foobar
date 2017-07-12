import decimal
import math
import matplotlib.pyplot as plt
decimal.getcontext().prec = 102
def answer(n):
    val = decimal.Decimal(n)
    sq2 = decimal.Decimal(2).sqrt()
    
    q = 1
    x = []
    y = []
    while q <= val:
        x += [q]
        y += [q * math.sqrt(2)]
        q += 1
    plt.plot(x,y)
    plt.show()




answer("77")


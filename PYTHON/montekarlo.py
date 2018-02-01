# -*- coding: utf-8 -*-
import random
import numpy as np
import matplotlib.pyplot as plt

def mans_sinussh(x):
    y = np.sinh(x)
    return y

N = 100000
x = []
y = []
a = 0.
b = np.pi
c = -4.
d = 4.

# -*- coding: utf-8 -*-
import random
import numpy as np
import matplotlib.pyplot as plt

def mans_sinussh(x):
    y = np.sinh(x)
    return y

N = 100000
x = []
y = []
a = 0.
b = np.pi
c = -4.
d = 4.

for i in range(N):
    x.append(random.uniform(a,b))
    #print "Kā veidojās x masīvs: ",x
for i in range(N):
    y.append(random.uniform(c,d))
    #print "Kā veidojās y masīvs: ",y

red_x = []
red_y = []
green_x = []
green_y = []

for i in range(N):
    if (y[i] < mans_sinussh(x[i]) and y[i] > 0) \
    or (y[i] > mans_sinussh(x[i]) and y[i] < 0):
        green_x.append(x[i])
        green_y.append(y[i])
    else:
        red_x.append(x[i])
        red_y.append(y[i])

plt.plot(green_x,green_y,'go')
plt.plot(red_x,red_y,'rv')
plt.grid()
plt.show()

areaRect = (b-a)*(d-c)
areaFunc = areaRect * len(green_x) / N
print areaFunc
print "Parāda cik laukuma vienības ir aizņēmusi funkcija sinh ar zaļajiem trijstūriem. Laukums tiek aprēķināts reizinot visu laukumu ar zaļajiem trijstūriem un dalot ar visiem punktiem"
for i in range(N):
    x.append(random.uniform(a,b))
    #print "Kā veidojās x masīvs: ",x
for i in range(N):
    y.append(random.uniform(c,d))
    #print "Kā veidojās y masīvs: ",y

red_x = []
red_y = []
green_x = []
green_y = []

for i in range(N):
    if (y[i] < mans_sinussh(x[i]) and y[i] > 0) \
    or (y[i] > mans_sinussh(x[i]) and y[i] < 0):
        green_x.append(x[i])
        green_y.append(y[i])
    else:
        red_x.append(x[i])
        red_y.append(y[i])

plt.plot(green_x,green_y,'go')
plt.plot(red_x,red_y,'rv')
plt.grid()
plt.show()

areaRect = (b-a)*(d-c)
areaFunc = areaRect * len(green_x) / N
print areaFunc
print "Parāda cik laukuma vienības ir aizņēmusi funkcija sin ar zaļajiem trijstūriem. Laukums tiek aprēķināts reizinot visu laukumu ar zaļajiem trijstūriem un dalot ar visiem punktiem"

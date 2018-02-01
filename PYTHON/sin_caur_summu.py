# -*- coding: utf-8 -*-
from math import sin

def mans_sinuss(x):
    k = 0
    a = (-1)**0*x**1/(1)
    S = a
    print "Izdruka no liet.f.a0 = %6.2f S0 = %6.2f"% (a,S)

    while k < 3: 
        k =k + 1 
        a = a * (-1) * x **2/((2*k)*(2*k+1))
        S = S + a
        print "Izdruka no liet.f.a%d = %6.2f S%d = %6.2f"% (k,a,k,S)
        print "Beigas!"
        return S

x = 1.*  input("Izdruka no galv.f.Lietotāj, lūdzu, ievadi x argumentu (x): ")
y = sin(x)
print "Izdruka no galv.f.standarta sin(%6.2f) = %6.2f"%(x,y)
yy = mans_sinuss(x)
print "Izdruka no galv.fmans sin(%6.2f) = %6.2f"%(x,yy)

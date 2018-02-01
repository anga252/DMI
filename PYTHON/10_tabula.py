#!/usr/bin/python

x = input("Ievadi x: ")
print "x = ", (x)
print "x || \t%1 | \t%2 | \t%3 | \t%4 | \t%5 | \t%10"
print "---------------------------------------------"
z=0
while (z < 11):
    a = x%1
    b = x%2
    c = x%3
    d = x%4
    e = x%5
    f = x%10
    print "%3d |%5d%8d%8d%8d%8d%8d"%(x,a,b,c,d,e,f)
    z=z+1
    x=x+1

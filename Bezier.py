from graphics import *
import numpy

def factorial(n):
    x = 1
    for i in range(1,n+1):
        x = x * i
    return x

def newton(n,i):
    return factorial(n)/(factorial(i)*factorial(n-i))

def Bezier(n,px,py):
    pointx=0
    pointy=0
    for t in numpy.arange(0.0,1.0,0.001):
        pointx = 0
        pointy = 0
        for i in range(n+1):
            pointx = pointx + (newton(n,i)*((1-t)**(n-i))*(t**i))*px[i]
            pointy = pointy + (newton(n,i)*((1-t)**(n-i))*(t**i))*py[i]
        pt = Point(pointx,pointy)
        pt.draw(win)


win = GraphWin('Inicjaly', 500, 500)

x = [48,43,73,130,198,189,185]
y = [358,372,134,135,136,374,360]
Bezier(5,x,y)

x2 = [55,190]
y2 = [250,250]
Bezier(1,x2,y2)

x3 = [277,277,296,281,268,524,287]
y3 = [341,356,145,140,135,188,243]
Bezier(6,x3,y3)


win.getMouse()
win.close()

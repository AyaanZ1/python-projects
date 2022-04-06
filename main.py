#graph a line
import matplotlib.pyplot as plt
import numpy as np
def quadratic(x,a,b,c):
    return a*x**2+b*x+c
def linear(x,a,b):
    return a*x+b
def exponential(x,a,b):
    return a*(b**x)
def absolute(x,a,b):
    return a*np.abs(x)+b


type = input("type of function(q to quit): ")
while type != "q":
    if type == "quadratic":
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
        x = np.linspace(-10,10, 50)
        y = quadratic(x,a,b,c)
        plt.plot(x,y)
        plt.grid()
        plt.show()
        type = input("type of function(q to quit): ")
    elif type == "linear":
        a = float(input("a: "))
        b = float(input("b: "))
        x = np.linspace(-10,10, 50)
        y = linear(x,a,b)
        plt.plot(x,y)
        plt.grid()
        plt.show()
        type = input("type of function(q to quit): ")
    elif type == "exponential":
        a = float(input("a: "))
        b = float(input("b: "))
        x = np.linspace(-10,10, 50)
        y = exponential(x,a,b)
        plt.plot(x,y)
        plt.grid()
        plt.show()
        type = input("type of function(q to quit): ")
    elif type == "absolute":
        a = float(input("a: "))
        b = float(input("b: "))
        x = np.linspace(-10,10, 50)
        y = absolute(x,a,b)
        plt.plot(x,y)
        plt.grid()
        plt.show()
        type = input("type of function(q to quit): ")
    elif type == "q":
        break
    else:
        print("invalid input")
        type = input("type of function(q to quit): ")



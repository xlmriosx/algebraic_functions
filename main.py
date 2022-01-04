import matplotlib.pyplot as plt
import numpy as np
from math import pi

N = 100 # number of points

## Linear function
def f(m,x,b):
  return m*x + b

m = (7-6)/(3-2)

# Limit domain
x = np.linspace(-10.0, 10.0, num=N)

b = 10

y = f(m,x,b)


fig, ax = plt.subplots()

ax.plot(x, y)
ax.grid()
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')

plt.show()

## Polinomic function

def f(x):
  return 2*x**7 - x**4 + 3*x**2 + 4

x = np.linspace(-100.0, 100.0, num=N)

y = f(x)

fig, ax = plt.subplots()
#Limit the function
plt.xlim(-25, 25)
plt.ylim(-15, 15)


ax.plot(x, y)
ax.grid()
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')
plt.show()

### Trascendent function
## trigonometric function

def f(x):
  return np.sin(x)

x = np.linspace(-2*pi, 2*pi, N)

y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid()
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')
plt.show()

## Exponential function
def f(x):
  return np.e**x

x = np.linspace(-1, 1, num=100000)

y = f(x)

delta = 0.01

fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid()
ax.set_ylim(1 - delta,1 + delta)
ax.set_xlim(0 - delta, 0 + delta)
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')
plt.show()


## Logaritmic function
def f(x):
  return np.log10(x)

x = np.linspace(0.01, 1000, num=N)

y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid()
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')
plt.show()


## Step function
def H(X):
  Y = np.zeros(len(X))
  for idx,x in enumerate(X):
    if x>=0:
      Y[idx] = 1.0
  return Y

# Datos para graficación

N = 1000

X = np.linspace(-1,1, num=N)

y = H(X)

fig, ax = plt.subplots()
ax.plot(X, y)
ax.grid()
plt.show()
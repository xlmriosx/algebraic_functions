import numpy as np
import matplotlib.pyplot as plt
from math import pi

N = 100 # número de puntos

# linear function
def f(m,x,b):
  return m*x + b


m = (7-6)/(3-2)

x = np.linspace(-10.0, 10.0, num=N)

b = 10

y = f(m,x,b)


fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid()
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')

# polinomic function
def f(x):
  return 2*x**7 - x**4 + 3*x**2 + 4

x = np.linspace(-100.0, 100.0, num=N)

y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid()
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')

# trigonometric function
def f(x):
  return np.sin(x)

x = np.linspace(-2*pi, 2*pi, N)

y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid()
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')

# exponential function
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

# logaritmic function

def f(x):
  return np.log10(x)

x = np.linspace(0.01, 1000, num=N)

y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid()
ax.axhline(y=0, color='r')
ax.axvline(x=0, color='r')

# step function

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

## Par function
def f(x):
    return np.cos(x)


# x = np.linspace(-10,10, num=1000)
#
#
fig, ax = plt.subplots()

# ax.plot(x, f(x))
# ax.grid()
# plt.show()

# ax.plot(x, f(-x))
# ax.grid()
# plt.show()

## Unpar function
def f(x):
    return np.sin(x)


# x = np.linspace(-10,10, num=1000)

# ax.plot(x, f(x))
# ax.grid()
# plt.show()

# ax.plot(x, -f(-x))
# ax.grid()
# plt.show()

## Monotonous function
# The function is monotonous and strictly increasing
def f(x):
    return x


# x = np.linspace(-10, 10, num=1000)
#
# ax.plot(x, f(x))
# ax.grid()
# plt.show()

# The function is monotonous and strictly decreasing
def f(x):
    return -x


# x = np.linspace(-10, 10, num=1000)
#
# ax.plot(x, f(x))
# ax.grid()
# plt.show()

# The function is monotonous and increasing
def f(x):
    return np.e**x


# x = np.linspace(-10, 10, num=1000)
#
# ax.plot(x, f(x))
# ax.grid()
# plt.show()

# The function is monotonous and decreasing
def f(x):
    return 1/x


# x = np.linspace(0, 10, num=1000)
#
# ax.plot(x, f(x))
# ax.grid()
# plt.show()

# The periodic function
def f(x):
    return np.sin(x)
#
# x = np.linspace(-10, 10, num=1000)
# ax.plot(x, f(x))
# ax.grid()
# plt.show()


# Convex
def f(x):
    return x**2

# x = np.linspace(-10, 10, num=1000)
# ax.plot(x, f(x))
# ax.grid()
# plt.show()

# Concave
def f(x):
    return -x**2

x = np.linspace(-10, 10, num=1000)
ax.plot(x, f(x))
ax.grid()
plt.show()




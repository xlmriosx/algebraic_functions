import numpy as np
import matplotlib.pyplot as plt


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




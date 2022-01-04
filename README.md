# Algebraic functions

## Linear function

![image](https://user-images.githubusercontent.com/78567418/148075363-3f86468b-1c78-4a44-ad0f-63a2c2569ea5.png)

![image](https://user-images.githubusercontent.com/78567418/148070314-59249630-a6e6-4164-bbc8-80a6721825b5.png)

## Polinomic function

![image](https://user-images.githubusercontent.com/78567418/148075400-b51cb618-24b5-4b93-a985-a5d5249c2b8b.png)

### Power function

![image](https://user-images.githubusercontent.com/78567418/148075443-3c798576-49d9-4e85-a495-e19cd587e658.png)

![image](https://user-images.githubusercontent.com/78567418/148072159-587275f1-d40e-42e0-9f2f-5ebe72a5da52.png)

## Trascendent function

Are functions that can't be expressed by polinomics function.

### Trigonometric function

![image](https://user-images.githubusercontent.com/78567418/148075479-5a292e1a-7703-4eaa-8a34-a51e15b07664.png)

![image](https://user-images.githubusercontent.com/78567418/148072575-ecf8bb3d-3fc7-4ddf-92f3-745a2567ead6.png)

### Exponential function

![image](https://user-images.githubusercontent.com/78567418/148075515-f9f75477-53c4-4e66-8e59-96e168d62db9.png)

![image](https://user-images.githubusercontent.com/78567418/148073107-e55ca991-a687-453d-9e38-94556c7900b1.png)

### Logaritm function

![image](https://user-images.githubusercontent.com/78567418/148075562-b9f3086e-580a-403a-b213-03c7645cc8f0.png)

![image](https://user-images.githubusercontent.com/78567418/148073780-6209c846-9a9c-4b8d-9566-f1528f2e599f.png)

## Seccionated function

![image](https://user-images.githubusercontent.com/78567418/148075606-c6e7f562-b190-44ef-9213-81e434fc7f92.png)

![image](https://user-images.githubusercontent.com/78567418/148074186-33e455f4-6760-4a61-8093-cca935fa27e8.png)

## Properties

### Par function

A function is even if it fulfills the following relation throughout its domain:

f(x) = f(-x)

If you noticed, this relationship tells us that a function is even if it is symmetric to the vertical axis (Y axis). For example, a parabola is a function is even.

f(x)

![image](https://user-images.githubusercontent.com/78567418/148107208-da41437e-1fc6-4a0f-948d-54ddd16af564.png)

f(-x)

![image](https://user-images.githubusercontent.com/78567418/148107231-82f19e46-a7ff-4350-8603-5b3e9f3825c4.png)


### Unpar function

A function is odd if it fulfills the following relation throughout its domain:

f(x) = -f(-x)

This relationship tells us that a function is odd if it is symmetric to the horizontal axis (X axis). For example, a cubic function is odd.

The two previous characteristics or properties are closely related to symmetry. You can check them yourself with different functions and even make a little routine in Python that checks if a function is odd or even.

f(x)

![image](https://user-images.githubusercontent.com/78567418/148107502-54a950a3-0382-475d-8377-9154fbbffce1.png)


-f(x)

![image](https://user-images.githubusercontent.com/78567418/148107555-088f9b4f-3bb8-4b5f-91b8-cfce39c2fc73.png)


### Bounded function

A function is bounded if its codomain (also known as range or image) is between two values, that is, it is bounded. This definition is defined as that there is a number m that, for every value of the domain of the function, holds that:

-m <= f(x) <= m

For example, the sine or cosine functions are bounded on the interval [-1, 1] within their co-domain.

### Monotonous function

These functions are useful to recognize or analyze because they allow us to know if a function increases or decreases in any of its intervals. That something is monotonous means that it has no variations. Then the monotonic functions are those that, within an interval I, belonging to the real numbers, fulfill any of these properties:

1. The function is monotonous and strictly increasing:
"If for all x1 and x2 that belong to the interval I, such that x1 is less than x2, if and only if f(x1) is less than f(x2)". In much simpler words, what this definition tells us is that x1 always has to be less than x2 in our interval I, and that when evaluating x2 in the function the result of this will always be greater than if we evaluate the function in x1. For the next three remaining definitions, the way they are interpreted does not change much.

![image](https://user-images.githubusercontent.com/78567418/148109034-6997e630-4f49-456d-8a6d-48811bd379e5.png)

2. The function is monotonous and strictly decreasing:
"If for all x1 and x2 that belong to the interval I, such that x1 is less than x2, if and only if f(x1) is bigger than f(x2)"

![image](https://user-images.githubusercontent.com/78567418/148109083-91c581c9-534e-4adc-876e-9b5744c6a071.png)

3. The function is monotonous and increasing:
"If for all x1 and x2 that belong to the interval I, such that x1 is less than x2, if and only if f(x1) is less than or equal f(x2)"

![image](https://user-images.githubusercontent.com/78567418/148109381-0c7fec4e-62e9-4a71-8d7f-cfe9dceff855.png)

4. The function is monotonous and decreasing:
"If for all x1 and x2 that belong to the interval I, such that x1 is less than x2, if and only if f(x1) is bigger than or equal f(x2)"

![image](https://user-images.githubusercontent.com/78567418/148109670-eac50ac5-4d1b-4601-976f-c5a888827457.png)

## Periodic functions

The periodic functions are those that are repeated every certain period, this period is called with the letter T. The relation that the function must fulfill to be periodic is the following.

f(x) = f(x + T), T <> 0

For example, the sine and cosine functions are periodic functions with a period T = 2π. In other words, if we calculate f(x) and we calculate f(x + 2π) in the sine function, the value that both expressions give us is the same.

![image](https://user-images.githubusercontent.com/78567418/148111114-0f85d2cc-70e6-4563-b71a-da664c65a55e.png)

## Concave and convex functions

Proving the concavity of a function can be done through consecutive derivative analysis, but we're not there yet, so don't worry. Here is a super intuitive way to see if a function is concave or convex.

A function within an interval is said to be convex if the function "opens up." That is, if it looks the following way:

![image](https://user-images.githubusercontent.com/78567418/148111522-2b51b0cc-50d3-4b94-9c31-5710f45b6833.png)

Now what would a concave function be? Well that's right, the opposite of a convex. A function within an interval is said to be concave if the function "opens downward." That is, if it looks the following way:


![image](https://user-images.githubusercontent.com/78567418/148111583-73a1b9f7-8088-41ca-b73d-401c5ffdda35.png)



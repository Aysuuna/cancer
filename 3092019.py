def series(n):
    total = 0
    for i in range (1, n + 1):
        total += i
    return total


def factorial(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
    return total

def digit_sum(n):
    while n >= 10:

        print()
    else:
        print(n)

def divisors(n):
    total = 0
    for i in range(1, n + 1):
        if n % i == 0:
            total += 1
        return total

print(divisors(1024))
#print (factorial(0))
# print(series(10))
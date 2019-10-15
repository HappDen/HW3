fib1 = 0
fib2 = 1
fib3 = 1
fib4 = 2
n = int(input())

for i in range(0, n):
    fib1 = fib1 + fib2
    fib2 = fib1 + fib2
    fib3 = fib3 + fib4
    fib4 = fib3 + fib4
    a = fib1
    b = fib3
    if a < n and b > n:
        print(b)

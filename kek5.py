fib1 = 0
fib2 = 1
fib3 = 1
fib4 = 2
n = int(input())

if n < 2:
    quit()

for i in range(2, n):
    fib1 = fib1 + fib2
    fib2 = fib1 + fib2
    fib3 = fib3 + fib4
    fib4 = fib3 + fib4
    a = fib1 + fib2
    b = fib3 + fib4
    if a <= n and b >= n:
        print(b)
    
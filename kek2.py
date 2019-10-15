Y = int(input())
X = int(input())
for a in range(1, Y // 20 + 1):
    for c in range(( Y - 20 * a ) // 10 + 1):
        t = X - a - c
        if 20 * a + 10 * c + 5 * t == Y:
            print(a, c, t) 
x1 = 0
y2 = 1
 
n = int(input())
 
if n < 2:
    quit()
 
print(x1, end=', ')
print(y2, end=', ')
for i in range(2, n):
    x1, y2 = y2, x1 + y2
    print(y2, end=', ')
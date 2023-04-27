a = 10
b = 5
c = 15

if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a

print(a, b, c)

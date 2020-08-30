x = [1, 17, 3, 5, 6, 8, 34, 32, 121, 11, 9, 13]
c = 0
a = 0
while a != len(x):
    if c < x[a]:
        c = x[a]
    else:
        c = c
    a = a + 1
print(c)    
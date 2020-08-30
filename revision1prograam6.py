x = [1, 17, 3, 5, 6, 8, 34, 32, 121, 11, 9, 13]
y = int(input("enter an integer"))
b = 0
while b < len(x) and x[b]!= y:
    if x[b] == y:
        print(x[b])
    b = b + 1
if b == len(x):
    print('"not exist"')
else:
    print(b,x[b])
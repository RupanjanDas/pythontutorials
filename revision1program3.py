a = int(input("enter a number:"))
b = int(input("enter a number:"))
c = int(input("enter a number:"))
d = a - b
if c == 0:
    print("error")
elif b >= a:
    print("error")
else:
    e = d%c
    print(e)
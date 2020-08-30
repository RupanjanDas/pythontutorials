t = int(input("enter a temperature"))
if t >= 104:
    print("high fever")
elif t < 104 and t >= 100:
    print("fever") 
elif t < 100 and t >= 98:
    print("mild fever")
else:
    print("no fever")


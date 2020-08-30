a = int(input("enter a number:"))
b = int(input("enter a number:"))
c = int(input("enter a number:"))
if a > b:
    print("case 1 = True")
    
if (a - c) >= (b - c):
    print("case 2 = True")
    
if ((a + c) * (b + c)) >= 100:
    print("case 3 = True")
    
if (a < b) and (not (b > c)):
    print("case 4 = True")
    
if (a == (b - 10)) or  (a != (c - 20)):
    print("case 5 = True")
    
if not (((a - b) < 10) and ((a + b) > c)):
    print("case 6 = True")
    
if not((a > b) or not(a > c)):
    print("case 7 = True")

def sgueeze (s):
    new = ""
    for i in s:
        if i != " ":
            new = new + i
        else:
            new = new
    return new
def ispalindrome (s):
    s = sgueeze(s)
    i = 0
    j = len(s) - 1       
    while i <= j:
        if s[i] != s[j]:   
            return False
        i = i + 1
        j = j - 1
    return True
print("This program checks if a word is Palindrome or not")
a = input("enter a word:")
b = input("enter a word:")
print(ispalindrome(a))   
print(ispalindrome(b))  
    
    
    
    
    
    
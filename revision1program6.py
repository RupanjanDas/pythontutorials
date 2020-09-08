x = [1, 17, 3, 5, 6, 8, 34, 32, 121, 11, 9, 13]
e = len(x)
i = 0
while i < e:
    j = i + 1
    while j < e:
        if x[i] > x[j]:
            a = x[i]
            x[i] = x[j]
            x[j] = a
        j += 1    
    i += 1

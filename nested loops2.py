rows = 0
b = 0
for i in range (rows, 5, 1):
    b += 1
    for j in range (0,i+1):
        print(b,end=' ')
    print('\r')
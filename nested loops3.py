rows = 5
b = rows-1
for i in range (0, rows, 1):
    for j in range (0, b):
        print(end=" ")
    b=b-1
    for j in range(0, i+1):
        print('*', end=" ")
    print('\r')
inp = input("Nhập x, y:")
di = [int(i) for i in inp.split(",")]
x, y = di[0], di[1] 
multiply = [[0 for i in range(y)] for j in range(x)]
for i in range(x):
    for j in range(y):
       multiply[i][j] = i * j
print(multiply)
#N = [int(i) for i in input("Введи число, например 01011011:")]
N = [1, 1, 1, 0, 1, 0, 1, 0]

B = [[0]*(len(N)-i) for i in range(len(N))]

tabl = ["0 0 0","0 0 1","0 1 0","0 1 1","1 0 0","1 0 1","1 1 0","1 1 1"]
mono = ["1", "z", "y", "yz", "x", "xz", "xy", "xyz"]


B[0] = N.copy()

for i in range(len(N)-1):
    for j in range(len(B[i])-1):
        B[i+1][j] = ( B[i][j]+B[i][j+1] ) % 2

polynom = []

print(f"\n x y z   F{' '*(5)}Треугольник Паскаля \n{'-'*(35)}" )
for i in range(len(N)):
    print(f" {tabl[i]}   {N[i]} {' '*(5+i)} {' '.join(str(i) for i in B[i])} ")
    if B[i][0] == 1:
        polynom.append(mono[i])

print(f"\nF = {' + '.join(polynom)}")




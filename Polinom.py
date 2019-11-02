# N = [int(i) for i in input("Enter a number, for example 01011011:")]
N = [1, 1, 1, 0, 1, 0, 1, 0]

#Pascal's empty triangle generation
B = [[0]*(len(N)-i) for i in range(len(N))]
B[0] = N.copy()

#Polynomial Compilation Kit
mono = ["1", "z", "y", "yz", "x", "xz", "xy", "xyz"]
polynom = []

#Filling Pascal Triangle 
for i in range(len(N)-1):

    for j in range(len(B[i])-1):

        B[i+1][j] = ( B[i][j]+B[i][j+1] ) % 2



print(f"\n x y z   F{' '*(5)}Треугольник Паскаля \n{'-'*(35)}" )

for i in range(len(N)):

    t = bin(i)[2:].zfill(3)
    print(f" {' '.join(t)}   {N[i]} {' '*(5+i)} {' '.join(str(i) for i in B[i])} ")

    if B[i][0] == 1:

        polynom.append(mono[i])

print(f"\nF = {' + '.join(polynom)}")

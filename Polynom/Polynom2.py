N = [int(i) for i in input("Enter a number, for example 01011011:")]
#N = [1, 1, 1, 0, 1, 0, 1, 0]

#Pascal's empty triangle generation
B = [[0]*(len(N)-i) for i in range(len(N))]
B[0] = N.copy()

#Polynomial compilation Kit
mono = ["1", "z", "y", "yz", "x", "xz", "xy", "xyz"]
end = []
polynom = []

f = {
	0 : ['a0',0],
	1 : ['a0 + a3',0],
	2 : ['a0 + a2',0],
	3 : ['a0 + a2 + a3 + a6',0],
	4 : ['a0 + a1',0],
	5 : ['a0 + a1 + a3 + a5',0],
	6 : ['a0 + a1 + a2 + a4',0],
	7 : ['a0 + a1 + a2 + a3 + a4 + a5 + a6 + a7',0]
}

#Filling Pascal Triangle 
for i in range(len(N)-1):

    for j in range(len(B[i])-1):

        B[i+1][j] = ( B[i][j]+B[i][j+1] ) % 2

for i in range (len(N)):

	end.append(B[i][0])
	t = bin(i)[2:].zfill(3)
	f[i][1] = N[i]
	print(f"F({','.join(t)}) = {f[i][0]} = {f[i][1]}")

print()

for i in range (len(N)):

	print(f"a{i} = {end[i]},", end = ' ')

	if end[i]:

		polynom.append(mono[i])

print(f"\nF = {' + '.join(polynom)}")

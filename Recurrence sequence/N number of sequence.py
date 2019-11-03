def get_a(N):
    a = [[0]*len(N) for i in range(len(N))]
    a[0] = N
    for i in range(1,len(N)):
        a[i][i-1] = 1
    return a

def get_identity(num):
    ret = [[0]*num for i in range(num)]
    for i in range(num):
        ret[i][i] = 1
    return ret

def matrix_pow(left, right, num):
    ret = get_identity(num)
    for i in range(num):
        for j in range(num):
            ret[i][j] = 0
            for k in range(num):
                ret[i][j] +=left[i][k]*right[k][j]
    return ret

def bin_pow(array, power, num):
    if power == 0:
        return get_identity(num)
    if power % 2:
        return matrix_pow(bin_pow(array, power - 1, num), array, num)
    else:
        b = bin_pow(array, power/2, num)
        return matrix_pow(b, b, num)

# From last to first
N = [int(i) for i in input("Enter the sequence coefficients by space: \n").split()[::-1]]
start_nums = [int(i) for i in input("Enter first numbers of sequence by space: \n").split()[::-1]]
Tn = int(input("Enter the desired member of the sequence: \n"))-1
answer = 0

new_matrix = bin_pow(get_a(N),Tn,len(N))

for i in range(len(N)):
    answer += new_matrix[len(N)-1][i] * start_nums[i]
print(f"T({Tn+1}) = {answer}")

class Matrix:
    def __init__(self, n, m, matrix):
        self.n = n
        self.m = m
        self.matrix = matrix

    def multiply(self, a):
        for i in range(self.n):
            for j in range(self.n):
                s = 0
                for k in range(self.m):
                    s += self.matrix[i][k] * a[k][j]
                print(s, end = " ")
            print()
    
t = int(input())
while t:
    inp = []
    while len(inp) < 2:
        inp += list(map(int, input().split()))
    n, m = inp[0], inp[1]
    a = []
    while len(a) < n:
        tmp = []
        while len(tmp) < m:
            tmp += list(map(int, input().split()))
        a.append(tmp)
    mat = Matrix(n, m, a)
    b = []
    for i in range(m) :
        x = []
        for j in range(n) :
            x.append(a[j][i])
        b.append(x)
    mat.multiply(b)
    t -= 1
     
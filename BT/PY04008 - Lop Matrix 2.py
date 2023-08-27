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
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    mat = Matrix(n, m, a)
    b = []
    for i in range(m) :
        x = []
        for j in range(n) :
            x.append(a[j][i])
        b.append(x)
    mat.multiply(b)
    t -= 1
     
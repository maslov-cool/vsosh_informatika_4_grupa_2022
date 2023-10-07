''' 1 способ
n, m, d = int(input()), int(input()), int(input())
A = [[int(input()), int(input())] for _ in range(d)]
B = [[0 for _ in range(n)] for _ in range(m)]
max = 0
for i in A:
    for x in range(i[0]):
        for y in range(i[1]):
            B[x][y] += 1
            if B[x][y] > max:
                max = B[x][y]
cnt = 0
for i in B:
    for j in i:
        if j == max:
            cnt += 1
print(cnt, d)'''

# 2 способ
n, m, d = int(input()), int(input()), int(input())
for i in range(d):
    n = min(int(input()), n)
    m = min(int(input()), m)
print(n * m, d)




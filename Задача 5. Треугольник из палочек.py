A, B, C = int(input()), int(input()), int(input())
A1 = []
for a in range(A, 0, -1):
    for b in range(B, 0, -1):
        for c in range(C, 0, -1):
            D = sorted([a, b, c])
            if D[2] >= D[0] + D[1]:
                A1.append(-sum(D) + A + B + C)
print(min(A1))



from itertools import permutations
letters = "SENDMORY"
for digits in permutations(range(10), 8):
    S, E, N, D, M, O, R, Y = digits
    if S == 0 or M == 0:
        continue
    SEND = S*1000 + E*100 + N*10 + D
    MORE = M*1000 + O*100 + R*10 + E
    MONEY = M*10000 + O*1000 + N*100 + E*10 + Y
    if SEND + MORE == MONEY:
        print("Solution:")
        print("S =", S)
        print("E =", E)
        print("N =", N)
        print("D =", D)
        print("M =", M)
        print("O =", O)
        print("R =", R)
        print("Y =", Y)
        print("\n", SEND)
        print("+", MORE)
        print("=", MONEY)
        break

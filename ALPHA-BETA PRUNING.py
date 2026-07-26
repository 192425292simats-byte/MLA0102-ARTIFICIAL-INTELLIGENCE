def alphabeta(depth, index, isMax, values, alpha, beta):
    if depth == 3:
        return values[index]
    if isMax:
        best = -1000
        for i in range(2):
            val = alphabeta(depth + 1, index * 2 + i, False,
                            values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = 1000
        for i in range(2):
            val = alphabeta(depth + 1, index * 2 + i, True,
                            values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best
print("Enter 8 leaf node values:")
values = list(map(int, input().split()))
result = alphabeta(0, 0, True, values, -1000, 1000)
print("Optimal value is:", result)

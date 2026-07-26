def minimax(depth, isMax, values):
    if depth == 3:
        return values.pop(0)
    if isMax:
        return max(minimax(depth + 1, False, values),
                   minimax(depth + 1, False, values))
    else:
        return min(minimax(depth + 1, True, values),
                   minimax(depth + 1, True, values))
print("Enter 8 leaf node values:")
values = list(map(int, input().split()))
result = minimax(0, True, values)
print("Optimal value is:", result)

from collections import deque
def water_jug(cap1, cap2, target):
    visited = set()
    queue = deque()
    queue.append((0, 0, []))
    while queue:
        jug1, jug2, path = queue.popleft()
        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))
        path = path + [(jug1, jug2)]
        if jug1 == target or jug2 == target:
            return path
        next_states = [
            (cap1, jug2),                 
            (jug1, cap2),                 
            (0, jug2),                  
            (jug1, 0),                   
            (jug1 - min(jug1, cap2-jug2),
             jug2 + min(jug1, cap2-jug2)),  
            (jug1 + min(jug2, cap1-jug1),
             jug2 - min(jug2, cap1-jug1))   
        ]
        for state in next_states:
            if state not in visited:
                queue.append((state[0], state[1], path))
    return None
cap1 = int(input("Enter capacity of Jug1: "))
cap2 = int(input("Enter capacity of Jug2: "))
target = int(input("Enter target amount: "))
result = water_jug(cap1, cap2, target)
if result:
    print("\nSteps:")
    for step in result:
        print(step)
else:
    print("No solution exists.")

monkey = "door"
box = "window"
banana = "ceiling"
actions = []
# Move monkey to box
actions.append("Monkey moves to the box")
# Push box to banana
actions.append("Monkey pushes the box under the banana")
# Climb box
actions.append("Monkey climbs onto the box")
# Get banana
actions.append("Monkey grabs the banana")
print("Optimal Action Plan:")
for i, action in enumerate(actions, 1):
    print(i, ".", action)

# 1. Check whether a color is safe
def isSafe(state, color, map, result):
    for neighbour in map[state]:
        if result.get(neighbour) == color:
            return False
    return True

# 2. Backtracking Algorithm
def backTrack(map, colors, result):
    # All states are colored
    if len(result) == len(map):
        return True

    # Select an uncolored state
    for state in map:
        if state not in result:
            break

    # Try every available color
    for color in colors:
        if isSafe(state, color, map, result):
            result[state] = color
            print("Assigned:", state, "->", color)

            if backTrack(map, colors, result):
                return True

            # Undo result (Backtracking)
            print("Backtracking:", state)
            del result[state]

    return False

# 3. Main Program
n = int(input("Enter number of states: "))
states = []
map = {}
for i in range(n):
    state = input("Enter state name: ")
    states.append(state)
    map[state] = []

e = int(input("Enter number of neighbouring pairs: "))
print("Enter neighbouring state pairs:")
for i in range(e):
    a, b = input().split()

    if a not in map or b not in map or a == b:
        print("Invalid neighbouring pair!")
        raise SystemExit

    map[a].append(b)
    map[b].append(a)

k = int(input("Enter number of colors: "))
colors = []
for i in range(k):
    colors.append(input("Enter color: "))

result = {}

# 4. Display Solution
if backTrack(map, colors, result):
    print("\\nMap Coloring Solution:")

    for state, color in result.items():
        print(state, ":", color)
else:
    print("No valid coloring possible!")

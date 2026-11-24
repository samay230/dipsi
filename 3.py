n = int(input("Enter number of states: "))

map = {}

for i in range(n):
    state = input("Enter state name: ")
    neighbors = input("Enter neighboring states (comma separated): ").split(",")

    map[state] = [x.strip() for x in neighbors]

# 2. Take available colors
colors = input("Enter available colors (comma separated): ").split(",")
colors = [c.strip() for c in colors]

# 3. Store assigned colors
result = {}

# 4. Check whether a color is safe
def is_safe(state, color):
    for neighbor in map[state]:
        if result.get(neighbor) == color:
            return False
    return True

# 5. Solve using Backtracking
def solve(index):
    if index == len(map):
        return True

    current = list(map.keys())[index]

    for color in colors:
        if is_safe(current, color):
            result[current] = color
            print(current, "->", color)

            if solve(index + 1):
                return True

            print("Backtracking:", current)
            del result[current]

    return False

# 6. Display the result
if solve(0):
    print("\nMap Coloring Solution:")
    for state, color in result.items():
        print(state, ":", color)
else:
    print("No solution exists!")
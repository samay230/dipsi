map = {
    "Maharashtra": ["Gujarat", "Madhya Pradesh", "Chhattisgarh", "Telangana", "Karnataka", "Goa"],
    "Gujarat": ["Maharashtra", "Madhya Pradesh", "Rajasthan"],
    "Madhya Pradesh": ["Gujarat", "Maharashtra", "Chhattisgarh", "Rajasthan", "Uttar Pradesh"],
    "Chhattisgarh": ["Maharashtra", "Madhya Pradesh", "Telangana", "Odisha", "Uttar Pradesh"],
    "Telangana": ["Maharashtra", "Chhattisgarh", "Karnataka", "Andhra Pradesh"],
    "Karnataka": ["Maharashtra", "Telangana", "Goa", "Andhra Pradesh"],
    "Goa": ["Maharashtra", "Karnataka"],
    "Rajasthan": ["Gujarat", "Madhya Pradesh", "Uttar Pradesh"],
    "Uttar Pradesh": ["Madhya Pradesh", "Chhattisgarh", "Rajasthan"],
    "Andhra Pradesh": ["Telangana", "Karnataka", "Odisha"]
}

result = {} #state : assigned color

colors = ["Red", "Green", "Blue", "Yellow"]


def isSafe(color, state, map, result):
    for neighbour in map[state]:
        if neighbour in result and result[neighbour] == color:
            return False
    return True


def backTrack(colors, map, result):
    # If all states are assigned a color
    if len(result) == len(map): #base case
        return True

    # Select an unassigned state
    for state in map:
        if state not in result:
            break

    # Try every available color
    for color in colors:
        if isSafe(color, state, map, result):
            result[state] = color

            if backTrack(colors, map, result):
                return True

            # Backtrack: remove the assignment
            del result[state]

    return False


if backTrack(colors, map, result):
    print("Map Colouring Solution\n")
    for state in result:
        print(state, ":", result[state])
else:
    print("No valid solution")

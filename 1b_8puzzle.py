import heapq

# 1. Heuristic function (Manhattan Distance)
def heuristic(state):
    distance = 0
    for i in range(9):
        tile = state[i]
        if tile != 0:
            row1, col1 = divmod(i, 3)
            row2, col2 = divmod(tile-1, 3)
            distance += abs(row1-row2) + abs(col1-col2)
    return distance

# 2. A* Algorithm
def astar(start):

    goal = (1, 2, 3, 
            4, 5, 6,
            7, 8, 0)
    pq = [(heuristic(start), 0, start, [])]
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)
        if state in visited:
            continue

        visited.add(state)
        path = path + [state]

        # Check goal
        if state == goal:
            return path

        # Find empty space
        zero = state.index(0)

        row = zero // 3
        col = zero % 3

        # Up, Down, Left, Right
        moves = [(-1,0), (1,0), (0,-1), (0,1)]

        for dr, dc in moves:
            r = row + dr
            c = col + dc

            if 0 <= r < 3 and 0 <= c < 3:
                new_pos = r * 3 + c
                new_state = list(state)

                # Swap empty space and tile
                new_state[zero], new_state[new_pos] = (
                    new_state[new_pos], new_state[zero]
                )
                new_state = tuple(new_state)

                if new_state not in visited:
                    new_g = g + 1
                    new_f = new_g + heuristic(new_state)

                    heapq.heappush(
                        pq, (new_f, new_g, new_state, path)
                    )
    return None

# 3. Main program
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)
solution = astar(start)
# 4. Display solution
if solution:
    print("Solution found!")
    print("Total moves:", len(solution)-1)

    for step, state in enumerate(solution):
        print("\nStep", step)
        for i in range(0, 9, 3):
            print(state[i:i+3])
else:
    print("No solution found")
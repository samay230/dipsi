import heapq

# 1. Heuristic Function: Manhattan Distance
def heuristic(state, goal, n):
    d = 0
    # Store the correct position of every tile
    goal_pos = {tile: i for i, tile in enumerate(goal)} # dictionary containing each tile's correct position

    for i, tile in enumerate(state):
        if tile != 0:
            j = goal_pos[tile]
            d += abs(i//n - j//n) + abs(i%n - j%n) #divmod --> for current & goal row & column

    return d

# 2. A* Algorithm
def astar(start, goal, n):
    # Priority queue: (f, g, state, path)
    pq = [(heuristic(start, goal, n), 0, start, ())]

    # Store the best cost found for each state
    best_g = {start: 0}
    
    while pq:
        f, g, state, path = heapq.heappop(pq)

        # Ignore an outdated queue entry
        if g != best_g[state]:
            continue

        path = path + (state,)

        # Goal reached
        if state == goal:
            return path

        # Find blank space
        zero = state.index(0)
        row, col = divmod(zero, n)

        # Up, Down, Left, Right
        moves = [(-1,0), (1,0), (0,-1), (0,1)]

        for dr, dc in moves:
            r, c = row + dr, col + dc

            if 0 <= r < n and 0 <= c < n:
                pos = r * n + c

                # Swap blank space with adjacent tile
                new_state = list(state)
                new_state[zero], new_state[pos] = new_state[pos], new_state[zero]
                new_state = tuple(new_state)

                new_g = g + 1

                if new_g < best_g.get(new_state, float('inf')):
                    best_g[new_state] = new_g
                    new_f = new_g + heuristic(new_state, goal, n)

                    heapq.heappush(
                        pq, (new_f, new_g, new_state, path) # type: ignore
                    )

    return None


# 3. Main Program
n = int(input("Enter N: "))
print("Enter initial state (0 for blank):")
start = []

for i in range(n):
    row = list(map(int, input().split()))
    start.extend(row)

print("Enter goal state:")
goal = []

for i in range(n):
    row = list(map(int, input().split()))
    goal.extend(row)

start = tuple(start)
goal = tuple(goal)
solution = astar(start, goal, n)

# 4. Display Solution
if solution:
    print("\nSolution Found!")
    print("Total Moves:", len(solution) - 1)

    for step, state in enumerate(solution):
        print("\nStep", step)
        for i in range(0, n*n, n):
            print(*state[i:i+n])
else:
    print("No solution found!")

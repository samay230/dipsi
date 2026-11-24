
import random

# 0 = Empty, 1 = Obstacle, 2 = Goal
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 2]
]

start = (0, 0)
goal = (4, 4)

# Actions: Up, Down, Left, Right
actions = [0, 1, 2, 3]

def move(state, action):
    r, c = state

    if action == 0: r -= 1
    elif action == 1: r += 1
    elif action == 2: c -= 1
    else: c += 1

    return (r, c)


# Check valid position
def is_valid(state):
    r, c = state
    return 0 <= r < 5 and 0 <= c < 5 and grid[r][c] != 1


# Reward function
def get_reward(state):
    if state == goal:
        return 100
    if not is_valid(state):
        return -10
    return -1


# Q-Table: 5 rows x 5 columns x 4 actions
Q = [[[0 for _ in actions] for _ in range(5)] for _ in range(5)]

def choose_action(state, epsilon):
    r, c = state

    if random.random() < epsilon:
        return random.choice(actions)       # Explore

    return Q[r][c].index(max(Q[r][c]))     # Exploit


# Q-Learning parameters
alpha = 0.1 #Learning rate
gamma = 0.9 #Importance of future rewards
epsilon = 1.0 #Initial exploration probability
episodes = 1000 #Training attempts

# Training
for episode in range(episodes):
    state = start

    for step in range(50):
        action = choose_action(state, epsilon)
        next_state = move(state, action)

        reward = get_reward(next_state)

        if not is_valid(next_state):
            next_state = state

        r, c = state
        nr, nc = next_state

        # Q-Learning update
        Q[r][c][action] += alpha * (
            reward + gamma * max(Q[nr][nc]) - Q[r][c][action]
        )

        state = next_state

        if state == goal:
            break

    epsilon = max(epsilon * 0.995, 0.05)


# Display learned path
state = start
path = [state]

for step in range(50):
    if state == goal:
        break

    r, c = state
    action = choose_action(state, 0)  # Greedy action
    next_state = move(state, action)

    if not is_valid(next_state) or next_state in path:
        print("Could not find a complete path.")
        break

    state = next_state
    path.append(state)
print("Learned Path:")
print(path)

if state == goal:
    print("Goal Reached!")
    print("Moves Taken:", len(path) - 1)
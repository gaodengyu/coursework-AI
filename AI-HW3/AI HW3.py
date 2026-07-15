import heapq
from copy import deepcopy

GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)
INIT_STATE = (1, 2, 6, 4, 0, 3, 5, 7, 8)

MOVES = {
    'up': -3,  
    'down': 3,  
    'left': -1, 
    'right': 1   
}

def is_solvable(state):
    tiles = [t for t in state if t != 0]
    inversions = 0
    for i in range(len(tiles)):
        for j in range(i+1, len(tiles)):
            if tiles[i] > tiles[j]:
                inversions += 1
    return inversions % 2 == 0

def misplaced_tiles(state):
    count = 0
    for i in range(9):
        if state[i] != 0 and state[i] != GOAL_STATE[i]:
            count += 1
    return count

def manhattan_distance(state):
    goal_pos = {}
    for i, val in enumerate(GOAL_STATE):
        if val != 0:
            goal_pos[val] = (i // 3, i % 3)
    dist = 0
    for i, val in enumerate(state):
        if val != 0:
            r, c = i // 3, i % 3
            gr, gc = goal_pos[val]
            dist += abs(r - gr) + abs(c - gc)
    return dist

def get_neighbors(state):
    zero_idx = state.index(0)
    neighbors = []
    for move, delta in MOVES.items():
        new_idx = zero_idx + delta
        if move == 'left' and zero_idx % 3 == 0:
            continue
        if move == 'right' and zero_idx % 3 == 2:
            continue
        if 0 <= new_idx < 9:
            new_state = list(state)
            new_state[zero_idx], new_state[new_idx] = new_state[new_idx], new_state[zero_idx]
            neighbors.append((tuple(new_state), move))
    return neighbors

def a_star(initial_state, heuristic):
    if not is_solvable(initial_state):
        return None, None, "不可解"

    open_set = []
    closed_set = set()
    g_score = {initial_state: 0}
    parent = {initial_state: (None, None)} 

    h = heuristic(initial_state)
    f = h
    heapq.heappush(open_set, (f, initial_state))

    while open_set:
        current_f, current_state = heapq.heappop(open_set)
        if current_state in closed_set:
            continue

        if current_state == GOAL_STATE:
            path = []
            state = current_state
            while parent[state][0] is not None:
                path.append(parent[state][1])
                state = parent[state][0]
            path.reverse()
            return g_score[current_state], path, "可解"

        closed_set.add(current_state)
        current_g = g_score[current_state]

        for neighbor, move in get_neighbors(current_state):
            if neighbor in closed_set:
                continue
            tentative_g = current_g + 1
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                h = heuristic(neighbor)
                f = tentative_g + h
                parent[neighbor] = (current_state, move)
                heapq.heappush(open_set, (f, neighbor))

    return None, None, "未找到解" 

def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

def main():
    print("初始状态：")
    print_state(INIT_STATE)

    if not is_solvable(INIT_STATE):
        print("该初始状态不可解！")
        return

    print("使用错位方块数启发式：")
    steps, path, msg = a_star(INIT_STATE, misplaced_tiles)
    if steps is not None:
        print(f"最短步数：{steps}")
        print("移动序列：", " -> ".join(path))
    else:
        print(msg)

    print("\n使用曼哈顿距离启发式：")
    steps, path, msg = a_star(INIT_STATE, manhattan_distance)
    if steps is not None:
        print(f"最短步数：{steps}")
        print("移动序列：", " -> ".join(path))
    else:
        print(msg)

if __name__ == "__main__":
    main()
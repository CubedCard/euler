from collections import deque

def bfs_max_path(triangle):
    queue = deque([(0, 0, triangle[0][0], [triangle[0][0]])])
    max_sum = triangle[0][0]
    best_path = [triangle[0][0]]

    while queue:
        row, col, current_sum, path = queue.popleft()

        if row == len(triangle) - 1:
            if current_sum > max_sum:
                max_sum = current_sum
                best_path = path
        else:
            if col < len(triangle[row + 1]):
                queue.append((row + 1, col, current_sum + triangle[row + 1][col], path + [triangle[row + 1][col]]))
            if col + 1 < len(triangle[row + 1]):
                queue.append((row + 1, col + 1, current_sum + triangle[row + 1][col + 1], path + [triangle[row + 1][col + 1]]))

    return max_sum, best_path

triangle = [[int(x) for x in line.split()] for line in open('input').read().splitlines()]

max_sum, best_path = bfs_max_path(triangle)

print(f"Maximum Path Sum: {max_sum}")
print(f"Path: {best_path}")

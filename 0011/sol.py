from functools import reduce

grid = [[int(x) for x in line.split()] for line in open('input').read().splitlines()]

def prod(nums):
    return reduce(lambda x, y: x * y, nums, 1)

def getMax(nums):
    r, m = 4, 0
    for i in range(len(nums) - r + 1):
        m = max(m, prod(nums[i:i + r]))
    return m

cols = [list(col) for col in zip(*grid)]

diags_tl_br = []
for i in range(len(grid)):
    diag = []
    x, y = i, 0
    while x < len(grid) and y < len(grid[0]):
        diag.append(grid[x][y])
        x += 1
        y += 1
    diags_tl_br.append(diag)

for i in range(1, len(grid[0])):
    diag = []
    x, y = 0, i
    while x < len(grid) and y < len(grid[0]):
        diag.append(grid[x][y])
        x += 1
        y += 1
    diags_tl_br.append(diag)

diags_tr_bl = []
for i in range(len(grid)):
    diag = []
    x, y = i, len(grid[0]) - 1
    while x < len(grid) and y >= 0:
        diag.append(grid[x][y])
        x += 1
        y -= 1
    diags_tr_bl.append(diag)

for i in range(len(grid[0]) - 2, -1, -1):
    diag = []
    x, y = 0, i
    while x < len(grid) and y >= 0:
        diag.append(grid[x][y])
        x += 1
        y -= 1
    diags_tr_bl.append(diag)

m = 0

for row in grid:
    m = max(m, getMax(row))

for col in cols:
    m = max(m, getMax(col))

for diag in diags_tl_br:
    m = max(m, getMax(diag))

for diag in diags_tr_bl:
    m = max(m, getMax(diag))

print(m)

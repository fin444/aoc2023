lines = [line.replace("\n", "") for line in open("input.txt", "r").readlines()]

nodes = [[False for j in range(1000)] for i in range(1000)]
boundaries = [0, 0]
pos = [0, 0]
count = 0
for line in lines:
    dist = int(line.split(" ")[1])
    if line[0] == "U":
        for i in range(dist):
            nodes[pos[0]][pos[1]] = True
            pos[0] -= 1
            count += 1
    elif line[0] == "D":
        for i in range(dist):
            nodes[pos[0]][pos[1]] = True
            pos[0] += 1
            count += 1
    elif line[0] == "L":
        for i in range(dist):
            nodes[pos[0]][pos[1]] = True
            pos[1] -= 1
            count += 1
    elif line[0] == "R":
        for i in range(dist):
            nodes[pos[0]][pos[1]] = True
            pos[1] += 1
            count += 1

filling = [[1, 1]]
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
while len(filling) != 0:
    new_filling = []
    for pos in filling:
        for dir in directions:
            new = [pos[0] + dir[0], pos[1] + dir[1]]
            if not nodes[new[0]][new[1]]:
                new_filling.append(new)
                nodes[new[0]][new[1]] = True
                count += 1
    filling = new_filling
print(count)

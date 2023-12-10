lines = [line.replace("\n", "") for line in open("input.txt", "r").readlines()]

pipes = {"|": [1, 0, -1, 0], "-": [0, 1, 0, -1], "L": [-1, 0, 0, 1], "J": [-1, 0, 0, -1], "7": [1, 0, 0, -1], "F": [1, 0, 0, 1], ".": [0, 0, 0, 0]}

# step 1: create the graph
nodes = []
S = []
for i in range(len(lines)):
	line = lines[i]
	line_nodes = []
	for j in range(len(line)):
		if line[j] == "S":
			line_nodes.append([])
			S = [i, j]
		else:
			char = pipes[line[j]]
			line_nodes.append([i + char[0], j + char[1], i + char[2], j + char[3]])
	nodes.append(line_nodes)

for i in range(len(nodes)):
	for j in range(len(nodes[0])):
		if [i, j] == S:
			continue
		if [nodes[i][j][0], nodes[i][j][1]] == S or [nodes[i][j][2], nodes[i][j][3]] == S:
			nodes[S[0]][S[1]] += [i, j]

# step 2: create the subpixel boundary layout
pos1 = [S, [nodes[S[0]][S[1]][0], nodes[S[0]][S[1]][1]]]
pos2 = [S, [nodes[S[0]][S[1]][2], nodes[S[0]][S[1]][3]]]
loop_nodes = [[False for j in range(len(nodes[0]) * 3)] for i in range(len(nodes) * 3)]

def add_node(pos):
	conn_node = nodes[pos[0]][pos[1]]
	conn = [pos[0] - conn_node[0], pos[1] - conn_node[1], pos[0] - conn_node[2], pos[1] - conn_node[3]]
	loop_nodes[pos[0] * 3 + 1][pos[1] * 3 + 1] = True
	loop_nodes[pos[0] * 3 + 1 - conn[0]][pos[1] * 3 + 1 - conn[1]] = True
	loop_nodes[pos[0] * 3 + 1 - conn[2]][pos[1] * 3 + 1 - conn[3]] = True

add_node(S)

while True:
	values = nodes[pos1[0][0]][pos1[0][1]]
	if values[0] == pos1[1][0] and values[1] == pos1[1][1]:
		pos1[1] = pos1[0]
		pos1[0] = [values[2], values[3]]
	else:
		pos1[1] = pos1[0]
		pos1[0] = [values[0], values[1]]
	values = nodes[pos2[0][0]][pos2[0][1]]
	if values[0] == pos2[1][0] and values[1] == pos2[1][1]:
		pos2[1] = pos2[0]
		pos2[0] = [values[2], values[3]]
	else:
		pos2[1] = pos2[0]
		pos2[0] = [values[0], values[1]]
	add_node(pos1[0])
	add_node(pos2[0])
	if pos1[0] == pos2[0]:
		break

# step 3: fill
filling = [[0, 0]]
loop_nodes[0][0] = True
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
while len(filling) != 0:
	new_filling = []
	for pos in filling:
		for dir in directions:
			new = [pos[0] + dir[0], pos[1] + dir[1]]
			if not loop_nodes[new[0]][new[1]]:
				new_filling.append(new)
				loop_nodes[new[0]][new[1]] = True
	filling = new_filling

# step 4: count empty spaces
empty = 0
for i in range(len(nodes)):
	for j in range(len(nodes[0])):
		valid = True
		for x in range(3):
			for y in range(3):
				if loop_nodes[i * 3 + x][j * 3 + y]:
					valid = False
		if valid:
			empty += 1
print(empty)

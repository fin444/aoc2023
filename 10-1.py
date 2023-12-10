lines = [line.replace("\n", "") for line in open("input.txt", "r").readlines()]

pipes = {"|": [1, 0, -1, 0], "-": [0, 1, 0, -1], "L": [-1, 0, 0, 1], "J": [-1, 0, 0, -1], "7": [1, 0, 0, -1], "F": [1, 0, 0, 1], ".": [0, 0, 0, 0]}

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

steps = 0
pos1 = [S, [nodes[S[0]][S[1]][0], nodes[S[0]][S[1]][1]]]
pos2 = [S, [nodes[S[0]][S[1]][2], nodes[S[0]][S[1]][3]]]
while True:
	steps += 1
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
	if pos1[0] == pos2[0]:
		break
print(steps)

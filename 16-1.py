lines = [line.replace("\n", "") for line in open("input.txt", "r").readlines()]

mirrors = {"/": {(0, 1): (-1, 0), (-1, 0): (0, 1), (0, -1): (1, 0), (1, 0): (0, -1)},
			"\\": {(0, 1): (1, 0), (1, 0): (0, 1), (-1, 0): (0, -1), (0, -1): (-1, 0)}}
splitters = {"|": (((0, 1), (0, -1)), ((1, 0), (-1, 0))), "-": (((1, 0), (-1, 0)), ((0, 1), (0, -1)))}
energized = []
beams = [(0, 0, 0, 1)]
while len(beams) != 0:
	new_beams = []
	for curr in beams:
		if curr not in energized:
			if curr[0] >= 0 and curr[0] < len(lines) and curr[1] >= 0 and curr[1] < len(lines[0]):
				energized.append(curr)
				char = lines[curr[0]][curr[1]]
				if char in mirrors:
					dir = mirrors[char][(curr[2], curr[3])]
					new_beams.append((curr[0] + dir[0], curr[1] + dir[1], dir[0], dir[1]))
				elif char in splitters and (curr[2], curr[3]) in splitters[char][0]:
					dirs = splitters[char][1]
					new_beams.append((curr[0], curr[1], dirs[0][0], dirs[0][1]))
					new_beams.append((curr[0], curr[1], dirs[1][0], dirs[1][1]))
				else:
					new_beams.append((curr[0] + curr[2], curr[1] + curr[3], curr[2], curr[3]))
	beams = new_beams

locs = []
for e in energized:
	loc = (e[0], e[1])
	if loc not in locs:
		locs.append(loc)
print(len(locs))

lines = [line.replace("\n", "") for line in open("input.txt", "r").readlines()]

empty_rows = []
empty_columns = []
for i in range(len(lines)):
	if len([a for a in lines[i] if a != "."]) == 0:
		empty_rows.append(i)
for i in range(len(lines[0])):
	if len([a for a in range(len(lines)) if lines[a][i] != "."]) == 0:
		empty_columns.append(i)

stars = []
for i in range(len(lines)):
	for j in range(len(lines[0])):
		if lines[i][j] == "#":
			stars.append([i + 999999 * len([a for a in empty_rows if a < i]), j + 999999 * len([a for a in empty_columns if a < j])])

total = 0
for i in range(len(stars)):
	star1 = stars[i]
	for star2 in stars[i + 1:]:
		total += abs(star1[0] - star2[0])
		total += abs(star1[1] - star2[1])
print(total)

lines = [line.replace("\n", "") for line in open("input.txt", "r").readlines()]
lines = list(reversed(lines))

def decreasing_add(start, count):
	if count == 0:
		return 0
	elif count == 1:
		return start
	return start + decreasing_add(start - 1, count - 1)

total = 0
for j in range(len(lines[0])):
	count = 0
	for i in range(len(lines)):
		if lines[i][j] == "#":
			total += decreasing_add(i, count)
			count = 0
		elif lines[i][j] == "O":
			count += 1
	total += decreasing_add(i + 1, count)
print(total)

lines = [line.replace("\n", "") for line in open("input.txt", "r").readlines()]

paths = {}
for line in lines[2:]:
	paths[line[0:3]] = [line[7:10], line[12:15]]

current = "AAA"
i = 0
while current != "ZZZ":
	if lines[0][i % len(lines[0])] == "L":
		current = paths[current][0]
	else:
		current = paths[current][1]
	i += 1
print(i)

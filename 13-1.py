lines = [line.replace("\n", "") for line in open("input.txt", "r").readlines()]

patterns = [[]]
for line in lines:
	if line == "":
		patterns.append([])
	else:
		patterns[-1].append(line)

total = 0
for pattern in patterns:
	# horizontal reflection
	for i in range(1, len(pattern)):
		top = list(reversed(pattern[:i]))
		bottom = pattern[i:]
		if top[:min(len(top), len(bottom))] == bottom[:min(len(top), len(bottom))]:
			total += i * 100
			break
	# vertical reflection
	for i in range(1, len(pattern[0])):
		left = list(reversed(["".join([line[j] for line in pattern]) for j in range(i)]))
		right = ["".join([line[j] for line in pattern]) for j in range(i, len(pattern[0]))]
		if left[:min(len(left), len(right))] == right[:min(len(left), len(right))]:
			total += i
			break
print(total)

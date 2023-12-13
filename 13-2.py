lines = [line.replace("\n", "") for line in open("input.txt", "r").readlines()]

patterns = [[]]
for line in lines:
	if line == "":
		patterns.append([])
	else:
		patterns[-1].append(line)

opposite = {"#": ".", ".": "#"}

def find_smudge(pattern):
	for i in range(1, len(pattern)):
		top = list(reversed(pattern[:i]))[:min(i, len(pattern) - i)]
		bottom = pattern[i:][:min(i, len(pattern) - i)]
		mismatches = 0
		for j in range(len(top)):
			if top[j] != bottom[j]:
				mismatches += 1
		if mismatches == 1:
			for j in range(len(top)):
				if top[j] != bottom[j]:
					for k in range(len(top[0])):
						if [top[j][a] if a != k else opposite[top[j][k]] for a in range(len(top[j]))] == list(bottom[j]):
							return i
					break
	return 0

total = 0
for pattern in patterns:
	total += 100 * find_smudge(pattern)
	total += find_smudge([list(i) for i in zip(*pattern)]) # transpose
print(total)

lines = [line.replace("\n", "") for line in open("input.txt", "r").readlines()]

total = 0
for line in lines:
	values = [[int(n) for n in line.split(" ")]]
	while sum(values[-1]) != 0:
		values.append([values[-1][i] - values[-1][i - 1] for i in range(1, len(values[-1]))])
	for i in reversed(range(1, len(values))):
		values[i - 1].append(values[i - 1][0] - values[i][-1])
	total += values[0][-1]
print(total)

lines = [line.replace("\n", "") for line in open("input.txt", "r").readlines()]

total = 0
for line in lines:
	groups = [int(n) for n in line.split(" ")[1].split(",")]
	springs = line.split(" ")[0]
	unknowns = [i for i in range(len(springs)) if springs[i] == "?"]
	for i in range(2**len(unknowns)):
		curr = springs
		counter = i
		for j in range(len(unknowns)):
			if counter % 2 == 0:
				curr = curr[:unknowns[j]] + "." + curr[unknowns[j] + 1:]
			else:
				curr = curr[:unknowns[j]] + "#" + curr[unknowns[j] + 1:]
			counter = counter // 2
		prev = "."
		build = []
		for char in curr:
			if char == "#":
				if prev == ".":
					build.append(1)
				else:
					build[-1] += 1
			prev = char
		if build == groups:
			total += 1
print(total)

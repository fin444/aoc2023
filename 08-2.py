lines = [line.replace("\n", "") for line in open("input.txt", "r").readlines()]

# shamelessly stolen from https://stackoverflow.com/a/22808285
def prime_factors(n):
	i = 2
	factors = []
	while i * i <= n:
		if n % i:
			i += 1
		else:
			n //= i
			factors.append(i)
	if n > 1:
		factors.append(n)
	return factors

paths = {}
for line in lines[2:]:
	paths[line[0:3]] = [line[7:10], line[12:15]]

times = []
for start in [j for j in paths.keys() if "A" in j]:
	current = start
	i = 0
	while "Z" not in current:
		if lines[0][i % len(lines[0])] == "L":
			current = paths[current][0]
		else:
			current = paths[current][1]
		i += 1
	times.append(i)

all_factors = []
total = 1
for time in times:
	factors = prime_factors(time)
	for f in factors:
		if f not in all_factors:
			all_factors.append(f)
			total *= f
print(total)

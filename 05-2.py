lines = [line.replace("\n", "") for line in open("input.txt", "r").readlines()]

ranges = []
split_seeds = lines[0].split(" ")[1:]
for i in range(len(split_seeds) // 2):
	ranges.append([int(split_seeds[i * 2]), int(split_seeds[i * 2]) + int(split_seeds[i * 2 + 1])])

new_ranges = []
for line in lines[3:]:
	if "-" in line:
		continue
	if line == "":
		ranges += new_ranges
		new_ranges = []
		continue
	conv = [int(x) for x in line.split(" ")]
	to_remove = []
	to_add = []
	for r in ranges:
		if r[0] < conv[1] + conv[2] and r[1] > conv[1]:
			to_remove.append(r)
			final = []
			if r[0] < conv[1]:
				to_add.append([r[0], conv[1]])
				final.append(conv[1] + conv[0] - conv[1])
			else:
				final.append(r[0] + conv[0] - conv[1])
			if r[1] > conv[1] + conv[2]:
				to_add.append([conv[1] + conv[2], r[1]])
				final.append(conv[1] + conv[2] + conv[0] - conv[1])
			else:
				final.append(r[1] + conv[0] - conv[1])
			new_ranges.append(final)
			continue
	for r in to_remove:
		ranges.remove(r)
	ranges += to_add

print(min([r[0] for r in ranges]))

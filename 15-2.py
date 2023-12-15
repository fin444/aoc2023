lines = [line.replace("\n", "") for line in open("input.txt", "r").readlines()]

def hash(string):
	value = 0
	for char in string:
		value += ord(char)
		value *= 17
		value = value % 256
	return value

hashmap = {}
for i in range(256):
	hashmap[i] = {}
for code in lines[0].split(","):
	label = code.split("=")[0].split("-")[0]
	h = hash(label)
	if code[len(label)] == "-":
		if label in hashmap[h]:
			del hashmap[h][label]
	else:
		hashmap[h][label] = code[len(label) + 1]

total = 0
for i in range(256):
	pos = 1
	for lens in hashmap[i]:
		total += (1 + i) * pos * int(hashmap[i][lens])
		pos += 1
print(total)

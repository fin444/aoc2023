lines = [line.replace("\n", "") for line in open("input.txt", "r").readlines()]

def hash(string):
	value = 0
	for char in string:
		value += ord(char)
		value *= 17
		value = value % 256
	return value

total = 0
for code in lines[0].split(","):
	total += hash(code)
print(total)

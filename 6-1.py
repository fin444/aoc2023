import math

lines = [line.replace("\n", "") for line in open("input.txt", "r").readlines()]

times = [int(n) for n in lines[0].split(" ")[1:] if n != ""]
distances = [int(n) + 0.01 for n in lines[1].split(" ")[1:] if n != ""]

total = 1
for i in range(len(times)):
	low = (-times[i] + math.sqrt(times[i]**2 - 4*1*distances[i])) / -2
	high = (-times[i] - math.sqrt(times[i]**2 - 4*1*distances[i])) / -2
	total *= math.floor(high) - math.ceil(low) + 1
print(total)

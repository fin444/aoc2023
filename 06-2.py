import math

lines = [line.replace("\n", "") for line in open("input.txt", "r").readlines()]

time = int(lines[0].replace(" ", "")[5:])
distance = int(lines[1].replace(" ", "")[9:])

low = (-time + math.sqrt(time**2 - 4*1*distance)) / -2
high = (-time - math.sqrt(time**2 - 4*1*distance)) / -2
print(math.floor(high) - math.ceil(low) + 1)

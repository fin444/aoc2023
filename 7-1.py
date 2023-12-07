lines = [line.replace("\n", "") for line in open("input.txt", "r").readlines()]
lines = [line.replace("A", "E").replace("K", "D").replace("Q", "C").replace("J", "B").replace("T", "A") for line in lines]

map = {}
for line in lines:
	map[line[0:5]] = int(line[6:])

hands = [[] for i in range(7)]
for hand in map:
	cards = {}
	for card in hand:
		if card in cards:
			cards[card] += 1
		else:
			cards[card] = 1
	counts = sorted(cards.values())
	if counts == [5]:
		hands[6].append(hand)
	elif counts == [1, 4]:
		hands[5].append(hand)
	elif counts == [2, 3]:
		hands[4].append(hand)
	elif counts == [1, 1, 3]:
		hands[3].append(hand)
	elif counts == [1, 2, 2]:
		hands[2].append(hand)
	elif counts == [1, 1, 1, 2]:
		hands[1].append(hand)
	else:
		hands[0].append(hand)

total = 0
count = 0
for thing in hands:
	for hand in sorted(thing):
		count += 1
		total += count * map[hand]
print(total)

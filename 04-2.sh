#! /usr/bin/env bash

cardNum=0
declare -a cardCounts=()
while read l; do
	cardCounts+=(1)
done < input.txt

while read l; do
	matches=0
	declare -a winning=($(echo "$l" | sed 's/|.*//' | sed 's/^.*: //'))
	declare -a have=($(echo "$l" | sed 's/^.*|//'))
	for i in ${have[@]}; do
		for j in ${winning[@]}; do
			[[ $i == $j ]] && (( matches += 1 ))
		done
	done
	for (( i = 1; i < matches + 1; i++ )); do
		(( cardCounts[cardNum + i] += cardCounts[cardNum] ))
	done
	(( cardNum += 1 ))
done < input.txt

total=0
for card in ${cardCounts[@]}; do
	(( total += card ))
done
echo $total

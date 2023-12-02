#! /usr/bin/env bash

total=0
gameNum=0
while read l; do
	((gameNum+=1))
	lastNum=0
	minRed=0
	minGreen=0
	minBlue=0
	for i in $l; do
		if [[ "$i" =~ [0-9]+ ]]; then
			lastNum=$i
		else
			max=0
			[[ "$i" == red* ]] && ((lastNum > minRed)) && minRed=$lastNum
			[[ "$i" == green* ]] && ((lastNum > minGreen)) && minGreen=$lastNum
			[[ "$i" == blue* ]] && ((lastNum > minBlue)) && minBlue=$lastNum
		fi
	done
	((total += minRed * minGreen * minBlue))
done < input.txt
echo $total

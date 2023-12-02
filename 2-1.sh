#! /usr/bin/env bash

total=0
gameNum=0
while read l; do
	((gameNum+=1))
	lastNum=0
	succeeded=true
	for i in $l; do
		if [[ "$i" =~ [0-9]+ ]]; then
			lastNum=$i
		else
			max=0
			[[ "$i" == red* ]] && max=12
			[[ "$i" == green* ]] && max=13
			[[ "$i" == blue* ]] && max=14
			(($lastNum > $max)) && succeeded=false
		fi
	done
	[[ $succeeded = true ]] && ((total+=gameNum))
done < input.txt
echo $total

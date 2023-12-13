#! /usr/bin/env bash

declare -a lines
while read l; do
	lines+=($l)
done < input.txt

total=0
for (( i=0; i<${#lines}; i++ )); do
	currNum=0
	valid=false
	for (( j=0; j<${#lines[0]}; j++ )); do
		if [[ "${lines[i]:j:1}" =~ [0-9] ]]; then
			(( currNum = currNum * 10 + ${lines[i]:j:1} ))
			(( i > 0 )) && [[ "${lines[(i-1)]:(j-1):3}" =~ [^0-9\.] ]] && valid=true
			[[ "${lines[i]:(j-1):3}" =~ [^0-9\.] ]] && valid=true
			(( i < ${#lines} - 1 )) && [[ "${lines[(i+1)]:(j-1):3}" =~ [^0-9\.] ]] && valid=true
		else
			[[ $valid = true ]] && (( total += currNum ))
			currNum=0
			valid=false
		fi
	done
	[[ $valid = true ]] && (( total += currNum ))
done
echo $total


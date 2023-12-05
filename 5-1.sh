#! /usr/bin/env bash

declare -a numbers
declare -a newSeeds
while read l; do
	if [[ "$l" == seeds* ]]; then
		numbers=($(echo "$l" | sed 's/seeds: //'))
		newSeeds=(${numbers[@]})
	elif [[ "${l:0:1}" =~ [0-9] ]]; then
		declare -a split=($l)
		for i in ${!numbers[@]}; do
			num=${numbers[$i]}
			(( num >= split[1] && num < split[1] + split[2] )) && (( newSeeds[i] += split[0] - split[1] ))
		done
	elif [[ "$l" == "" ]]; then
		numbers=(${newSeeds[@]})
	fi
done < input.txt

min=99999999999999
for n in ${numbers[@]}; do
	(( n < min )) && min=$n
done
echo $min

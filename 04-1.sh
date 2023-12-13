#! /usr/bin/env bash

total=0
while read l; do
	matches=-1
	declare -a winning=($(echo "$l" | sed 's/|.*//' | sed 's/^.*: //'))
	declare -a have=($(echo "$l" | sed 's/^.*|//'))
	for i in ${have[@]}; do
		for j in ${winning[@]}; do
			[[ $i == $j ]] && (( matches += 1 ))
		done
	done
	(( matches > -1 )) && (( total += 2**matches ))
done < input.txt
echo $total

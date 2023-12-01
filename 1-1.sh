#! /usr/bin/env bash

total=0
while read l; do
	first=0
	last=0
	for ((i=0; i<${#l}; i++)); do
		if [[ "${l:$i:1}" =~ [0-9] ]]; then
			[[ $first == 0 ]] && first=${l:$i:1} || last=${l:$i:1}
		fi
	done
	[[ $last == 0 ]] && last=$first
	total=$((total + "$first$last"))
done < input.txt
echo $total

#! /usr/bin/env bash

declare -a lines
while read l; do
	lines+=($l)
done < input.txt

declare -A gears=()
for ((i=0; i<${#lines}; i++)); do
	currNum=0
	declare -a adj=()
	for ((j=0; j<${#lines[0]}; j++)); do
		if [[ "${lines[i]:j:1}" =~ [0-9] ]]; then
			(( currNum = currNum * 10 + ${lines[i]:j:1} ))

			(( i > 0 )) && (( j > 0 )) && [[ "${lines[(i - 1)]:(j - 1):1}" == '*' ]] && adj+=("$((i - 1))-$((j - 1))")
			(( i > 0 )) && [[ "${lines[(i - 1)]:j:1}" == '*' ]] && adj+=("$((i - 1))-$j")
			(( i > 0 )) && [[ "${lines[(i - 1)]:(j + 1):1}" == '*' ]] && adj+=("$((i - 1))-$((j + 1))")

			(( j > 0 )) && [[ "${lines[$i]:(j - 1):1}" == '*' ]] && adj+=("$i-$((j - 1))")
			[[ "${lines[$i]:j:1}" == '*' ]] && adj+=("$i-$j")
			[[ "${lines[$i]:(j + 1):1}" == '*' ]] && adj+=("$i-$((j + 1))")

			(( j > 0 )) && [[ "${lines[(i + 1)]:(j - 1):1}" == '*' ]] && adj+=("$((i + 1))-$((j - 1))")
			[[ "${lines[(i + 1)]:j:1}" == '*' ]] && adj+=("$((i + 1))-$j")
			[[ "${lines[(i + 1)]:(j + 1):1}" == '*' ]] && adj+=("$((i + 1))-$((j + 1))")
		else
			for gear in "$(echo "${adj[@]}" | tr ' ' '\n' | sort -u | tr '\n' ' ')"; do
				[[ "$gear" != " " ]] && gears["$gear"]+="-$currNum"
			done
			currNum=0
			adj=()
		fi
	done
	for gear in "$(echo "${adj[@]}" | tr ' ' '\n' | sort -u | tr '\n' ' ')"; do
		[[ "$gear" != " " ]] && gears["$gear"]+="-$currNum"
	done
done

total=0
for gear in "${gears[@]}"; do
	echo $gear
	arr=(${gear//-/ })
	[[ ${#arr[@]} == 2 ]] && (( total += ${arr[0]} * ${arr[1]} ))
done
echo $total

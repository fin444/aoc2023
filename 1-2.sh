#! /usr/bin/env bash

total=0
while read l; do
	first=0
	last=0
	l=${l//one/on1e}
	l=${l//two/tw2o}
	l=${l//three/thr3ee}
	l=${l//four/fo4ur}
	l=${l//five/fi5ve}
	l=${l//six/si6x}
	l=${l//seven/se7ven}
	l=${l//eight/eig8ht}
	l=${l//nine/ni9ne}
	for ((i=0; i<${#l}; i++)); do
		if [[ "${l:$i:1}" =~ [0-9] ]]; then
			[[ $first == 0 ]] && first=${l:$i:1} || last=${l:$i:1}
		fi
	done
	[[ $last == 0 ]] && last=$first
	total=$((total + "$first$last"))
done < input.txt
echo $total

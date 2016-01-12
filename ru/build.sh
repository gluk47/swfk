#!/bin/bash -e

valid_targets=($(echo version-*.tex))
valid_targets=(${valid_targets[@]#version-})
valid_targets=(${valid_targets[@]%.tex})

build () {
	local os=$1
	[[ -e version-${os}.tex ]] || {
		echo "Skipping invalid target '$os'."
		echo "The list of valid targets is: ${valid_targets[@]}"
		return 1
	}
	ln -fs version-${os}.tex version.tex
	xelatex book.tex
	xelatex book.tex
	mv book.pdf book-${os}.pdf
}

targets="${1:-linux windows macos}"

for os in $targets; do
	build $os
done

#!/bin/bash -e

build () {
	local os=$1
	ln -fs version-${os}.tex version.tex
	xelatex book.tex
	xelatex book.tex
	mv book.pdf book-${os}.pdf
}

if [[ $1 ]]; then
	for os in "$@"; do
		build $os
	done
else
	for i in {1..2}; do
		for os in linux windows macos; do
			build $os
		done
	done
fi


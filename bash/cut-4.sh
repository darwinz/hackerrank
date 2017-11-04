#!/bin/bash
: '
Display the first four characters from each line of text.

Input Format

A text file with lines of ASCII text only.

Constraints

* 1 <= N <= 100

(N is the number of lines of text in the input file)

Output Format

The output should contain N lines. Each line should contain just the first four characters of the corresponding input line.

Sample Input

Hello
World
how are you
Sample Output

Hell
Worl
how
'

cut --characters=1-4 /dev/stdin

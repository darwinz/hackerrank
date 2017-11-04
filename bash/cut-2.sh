#!/bin/bash
: '
Display the 2nd and 7th character from each line of text.

Input Format

A text file with N lines of ASCII text only.

Constraints

Output Format

The output should contain  lines. Each line should contain just two characters at the 2nd and the 7th position of the corresponding input line.

Sample Input

Hello

World

how are you

Sample Output

e

o

oe
'

cut --characters=2,7 /dev/stdin

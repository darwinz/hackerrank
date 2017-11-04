#!/usr/bin/env bash

#We provide you with expressions containing +,-,*,^, / and parenthesis. None of the numbers in the expression involved will exceed 999.
#Your task is to evaluate the expression and display the output correct to 3 decimal places.
#
#Input Format
#
#-
#
#Constraints
#
#-
#
#Output Format
#
#-
#
#Sample Input
#
#Sample Input 1
#
#5+50*3/20 + (19*2)/7
#Sample Input 2
#
#-105+50*3/20 + (19^2)/7
#Sample Input 3
#
#(-105.5*7+50*3)/20 + (19^2)/7
#Sample Output
#
#Sample Output 1
#
#17.929
#Sample Output 2
#
#-45.929
#Sample Output 3
#
# 22.146
#Explanation
#
#-


read input
printf '%.$3f' `echo "scale=3; $input" | bc`
printf "%.3f" `echo "$input" | bc -l`
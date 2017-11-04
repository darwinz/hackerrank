#!/usr/bin/env bash

#Given a list of countries, each on a new line, your task is to read them into an array and then display the entire array, with a space between each of the countries' names.
#
#Recommended References
#Here's a great tutorial tutorial with useful examples related to arrays in Bash.
#
#Input Format
#
#A list of country names. The only characters present in the country names will be upper or lower case characters and hyphens.
#
#Output Format
#
#Display the entire array of country names, with a space between each of them.
#
#Sample Input
#
#Namibia
#Nauru
#Nepal
#Netherlands
#NewZealand
#Nicaragua
#Niger
#Nigeria
#NorthKorea
#Norway
#Sample Output
#
#Namibia Nauru Nepal Netherlands NewZealand Nicaragua Niger Nigeria NorthKorea Norway
#Explanation
#
#The entire array has been displayed.

while read line
do
  list=("${list[@]}" $line)
done
for a in "${list[@]}"
do
  echo -n "${a} "
done

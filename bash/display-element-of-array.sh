#Given a list of countries, each on a new line, your task is to read them into an array and then display the element indexed at . Note that indexing starts from .
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
#The element at index  of the array (one string).
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
#Netherlands
#Explanation
#
#The element at index  in the list is Netherlands.

list=$(cat)
list=( ${list[@]} )
echo ${list[3]}

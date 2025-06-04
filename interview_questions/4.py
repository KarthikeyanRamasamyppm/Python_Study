# Write a program that accepts a comma separated 
# sequence of words as input and prints the words in a comma-separated 
# sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# bag,hello,without,world
str_1="without,hello,bag,world"
str_2=list(str_1.split(","))
str_2.sort()
str_3=",".join(str_2)
print(str_3)



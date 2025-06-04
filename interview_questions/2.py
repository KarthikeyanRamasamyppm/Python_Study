# With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included).
# and then the program should print the dictionary.
# Suppose the following input is supplied to the program: 8
#method:1
dict_1={}
for i in range(1,9):
    dict_1.update({i:i*i})
print(dict_1)

dict_2={i:i*i for i in range(1,9)}
print(dict_2)
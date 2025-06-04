#hello world and practice makes perfect and hello world again
#again and hello makes perfect practice world
str_1="hello world and practice makes perfect and hello world again"
str_2=str_1.split()
print(str_2)
list_1=[]
for i in str_2:
    if i in list_1:
        pass
    else:
        list_1.append(i)
list_1.sort()
print(list_1)
txt="List are ordered and changeable ie mutable and allow duplicates"
print(txt)
#convert txt to list
s=txt.split()
print(s)

#create a empty list

fruits=[]
print(len(fruits))

# list with items

fruits1=["apple","orange","banana","mango"]
print(fruits1)

#len of the fruits1
print(len(fruits1)) 

# add one more fruit to the existing fruit

fruits1.append("kiwi")
print(fruits1)


cars=["Alto 800","celerio","s-presso"]
cars1=["Breeza","Iginis","ciaz"]
cars.extend(cars1)
print(cars)

#list methods:
a=[1,2,3,5,4]
print(a)
#sort method
a.sort()
print(a)
#reverse method
a1=[4,3,2,1]
a1.reverse()
print(a1)
print(a1[::-1])

#sum of list
print(sum(a1))

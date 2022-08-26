#sum of all even numbers from 1 to 100
sum=0
for x in range(1,101):
    # print(x)
    if(x%2==0):
        print(x)
        sum=sum+x
print(sum)
#using list method:
# new=input("Enter Your Maximum Number:")
# print(new)
newlist=[]
for y in range(1,101):
    if(y%2==0):
        newlist.append(y)
    print(newlist)
    print(sum(newlist))
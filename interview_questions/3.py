transactions=[
    {
        "name":"karthik",
        "amount":700
    },
    {
        "name":"shanmuga",
        "amount":800
    },
    {
        "name":"karthik",
        "amount":100
    }
]
list_1=[]
dict_1={}
for i in transactions:
    print(i)
    name=i["name"]
    if name in dict_1.keys():
        dict_1[name]["amount"]+=i["amount"]
    else:
        dict_1[name]={}
        dict_1[name]["name"]=i["name"]
        dict_1[name]["amount"]=i["amount"]
list_1.append(dict_1.values())
print(list_1)
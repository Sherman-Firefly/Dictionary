dict = {'name': 2, 'Age': 17, 'Place': 22, 'banana': 23, 'Apple': 17, 'Food': 50, 'orange': 2, 'pinapple': 17, 'pilot': 23}


a=int(input("Input a number"))
res=0
for i in dict:
    if dict[i]==a:
        res=res+1

print(f"frequency of dictionary", res)
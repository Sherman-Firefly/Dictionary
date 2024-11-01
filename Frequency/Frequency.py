dict = {'name': 2, 'Age': 17, 'Place': 22}

print(dict)

a=2
res=0
for i in dict:
    if dict[i]==a:
        res=res+1

print(f"frequency of dictionary", res)
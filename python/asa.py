data=[
    {'name':'Lalit','age':15},
    {'name':'suman','age':18},
    {'name':'Lalit','age':15},
    {'name':'suman','age':18},
    {'name':'suman','age':18},
    {'name':'suman','age':18},
    {'name':'a','age':12},
    {'name':'a','age':12},
    {'name':'a','age':12}
    ]
lis=[]
l=[]
count = 1
a=data.count()
for ele in data:
        a=data.count(ele)
        if a not in l:
            l.append(a)
        
print(l)
for ele in data:
    if ele not in lis:
        lis.append(ele)
         
for i in range(0,len(l)):
    lis[i]['count']=l[i]
print(lis)

ele = "GYBRGBBRR"
lis=[]
ept={}

for i in ele:
    lis.append(i)

for ele in lis:
    if ele not in ept:
        ept[ele]=0
        
    ept[ele] =ept[ele]+1
    print(ept)
print(ept)


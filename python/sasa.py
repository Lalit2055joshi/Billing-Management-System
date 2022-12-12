def fun(*args):
    sum=0
    for i in args:
        sum = sum+i
    return sum

# fun(2,3)
print(fun(2,3))
print(fun(2,3,5))

def country(self):
        # lis=[]
        ls = []
        value = set()
        
        for ele in self.data:
            value.add(ele['country'])
        for ele in self.data:
            y = {}
            for i in value:
                
                if i == ele["country"]:
                    y[i]=ele
                    ls.append(y)
        return ls
        
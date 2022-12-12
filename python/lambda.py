a=[10,50,60,454,67,45]
c=[1,2,3,4,54,6]
# result=list(filter(lambda a: a>=60 ,a))
# print(result)
# print(type(result))
# def inc(n):
#     return n+2
result = list(map(lambda a,c:a+c,a,c))
print(result)
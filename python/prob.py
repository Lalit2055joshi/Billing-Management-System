import json
f=open('/home/intern/Desktop/Django/python/data.json')
data = json.load(f) 

# print(data)
class Author():
    def __init__(self,data):
        self.data=data
    def search(self):
        for info in self.data:
            if info["pages"]>200:
                return(info)
            else:
                return("data does not exist")
    def sum_of_page(self):
        sum=0
        for ele in self.data:
            sum=sum+ele["pages"]
        return sum
    def sorting(self):
        lis = sorted(self.data, key=lambda k: k['title'])
        return(lis)
    def ydata(self):
        lis=[]
        li = []
        D1= dict({"greater 1950": lis})
        D2 = dict({"greater 1950": li})
        d3 = {**D1,**D2}
        
        for ele in self.data:
       
            if ele['year']>1950:
                lis.append(ele)
        
            else:
                li.append(ele)
        return d3
            
    # def country(self):
    #     ls=[]
    #     unique_countries = set()
    #     for ele in self.data:
    #         unique_countries.add(ele['country'])
    #     for unique_country in unique_countries:
    #         for item in self.data:
    #             if unique_country == item["country"]:
             
    #                 ls.append(dict({unique_country: item}))

        
    #     return ls
    def country(self):
        unique_countries = set(map(lambda x: x['country'],self.data))
        country_name={}
        for unique_country in unique_countries:
            country_name[unique_country]=list(filter(lambda x : x["country"] == unique_country,self.data))
        return country_name 


          
                

    



au = Author(data)
# print(au.search())
# print(au.sum_of_page())
# print(au.sorting())
# print(au.ydata)
# print(au.ydata())
print(au.country())

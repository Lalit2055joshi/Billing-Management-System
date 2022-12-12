from datetime import datetime
def presentdata(startdate,enddate,ad):
    datelist=[]  
    sum=0
    for i in range(0,len(ad)-1):
        if ad[i] >=startdate or ad[i]<=enddate:
            abd = ad[i+1] - ad[i]
            datelist.append(abd.days+1)
        print(abd.days+1)
    print(datelist)
    for i in range(0,len(datelist)):
        # print(datelist[i])
        if datelist[i]<=4:
            # print(datelist[i])
            sum=sum + datelist[i]
    print(sum)
    
str_d1 = '2021/10/20'
str_d2 = '2022/10/20'
absentdate=[]
dat=['2021/10/26','2021/10/27','2021/11/29','2021/12/1','2022/1/20']

for date in dat:
    absentdate.append(datetime.strptime(date,"%Y/%m/%d"))

startdate = datetime.strptime(str_d1, "%Y/%m/%d")
enddate = datetime.strptime(str_d2, "%Y/%m/%d")
a=enddate-startdate
# print(a.days)
presentdata(startdate,enddate,absentdate)


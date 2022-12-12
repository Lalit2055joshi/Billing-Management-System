import mysql.connector as a
con = a.connect(host="localhost",password="password",user="root",database="bank")
def openAcc():
    n = input("Enter your Name:")
    ac = input("Enter Account No:")
    db = input("Enter date of birth:")
    p=input("Enter Phone Number:")
    ad= input("Enter Address:")
    ob = int(input("Enter Opening Balance:"))
    data1=(n,ac,db,p,ad,ob)
    data2=(n,ac,ob)
    sql1 ='insert into account values(%s,%s,%s,%s,%s,%s)'
    sql2='insert into amount values(%s,%s,%s)'
    c=con.cursor()
    c.execute(sql1,data1)
    c.execute(sql2,data2)
    con.commit()
    print("Data Entered Sucessufully!!")
    main()
def depoAm():
    am=int(input("Enter Amount:"))
    ac=input("Enter Account No:")
    a = "select balance from amount where acno = %s"
    data = (ac,)
    c= con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    tam = myresult[0]+am
    sql = "update amount set balance=%s where acno=%s"
    d=(tam,ac)
    c.execute(sql,ac)
    con.commit()
    main()

def witham():
    am=int(input("Enter Amount:"))
    ac=input("Enter Account No:")
    a = "select balance from amount where acno = %s"
    data = (ac,)
    c= con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    tam = myresult[0]-am
    sql = "update amount set balance=%s where acno=%s"
    d=(tam,ac)
    c.execute(sql,ac)
    con.commit()
    main()
def balance():
    ac = input("Enter Account No:")
    a="select balance from amount where acno=%s"
    data = (ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult = c.fetchone()
    print("Balance for account:",ac,"is",myresult[0])
    main()
def dispacc():
    ac=input("Enter Account No:")
    a="select * from account where acno=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    for i in myresult:
        print(i,end="")
    main()
def closeac():
    ac=input("Enter Account No:")
    sql1="delete from account where acno=%s"
    sql2="delete from amount where acno=%s"
    data=(ac,)
    c=con.cursor()
    c.execute(sql1,data)
    c.execute(sql2,data)
    con.commit()
    main()


def main():
    print("""
    1. Open New Account 
    2.Deposit Amount
    3. Withdraw Amount
    4. Balance Enquiry
    5. Display Custumer Details
    6. Close an Account    """)
    choice = input("Enter the task number : ")
    if choice == '1':
        openAcc()
    elif choice == '2':
        depoAm()
    elif choice == '3':
        witham()
    elif choice == '4':
        balance()
    elif choice == '5':
        dispacc()
    elif choice == '6':
        closeac()
    else:
        print("Wrong Choice")
        main()
main()
from email.message import EmailMessage
import os
import ssl
import smtplib
from datetime import date
from datetime import date
import csv
import datetime
from email_validator import validate_email, EmailNotValidError
print("******Menu********")

def choose():
    choice = input('''
Enter your Choice
1.Customer 
2.Subscription
3.send email
4.Exit
input:-''')
    choice_1 = {'1':customer,'2':subscription,'3':send_email,'4':exit}
    if choice not in choice_1:
        print("Enter a valid number")
        return choose()
    choice_1.get(choice)()
    
    
def customer():
    print("Select the choice")
    choice_2=input('''
    Enter your choice
    1. Create Customer
    2.Retrive Customer
    3. Delete Customer
    4.List Customer
    5. Update 
    6. Exit 
    input:-''')
    choice={'1':create_customer,
    '2':retrive_customer,
    '3':delete_customer,
    '4':lis_customer,
    '5':update_customer,
    '6':exit}
    if choice_2 not in choice:
        print("Enter a valid number")
        return customer()
    choice.get(choice_2)()

    
def create_customer():
    Name=input("Enter your name:-")   
    Phone=int(input("Enter Your Phone Number:-"))
    Created_at = date.today()
    Status = input("Enter your status active or inactive enter:-")
    Email = input("Enter your email:-")
    check_valid_email(Email)
    # file_exists = os.path.isfile('subscription.csv')
    with open('/home/intern/Desktop/Django/BMS/customer.csv', mode='a+') as csv_file:
        fieldnames = ['Name', 'Email', 'Phone','Created_at','Status']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        if not  csv_file:
            writer.writeheader()
        writer.writerow({'Name': Name,
         'Email': Email, 
         'Phone':Phone,
         'Created_at':Created_at,
         'Status':Status})
    
        
def retrive_customer():
    search = input("Enter the customer Name:-")
    with open('/home/intern/Desktop/Django/BMS/customer.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Name'] == search:
                print(row)
    

def delete_customer():
    lines = list() 
    lines1=[]
    memberName = input("Please enter a member's name to be deleted:-")
    with open('/home/intern/Desktop/Django/BMS/customer.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == memberName:
                    lines.remove(row)
    with open('/home/intern/Desktop/Django/BMS/customer.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)
    with open('/home/intern/Desktop/Django/BMS/subcription.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines1.append(row)
            for field in row:
                if field == memberName:
                    lines1.remove(row)
    with open('/home/intern/Desktop/Django/BMS/subcription.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines1)

def lis_customer():
    print("***list choices****")
    choice_3 = input('''choice any one
    1.All data
    2.Active
    3.Exit
    input:-''')
    choice = {'1':all_data,'2':active_inactive,'3':exit}
    choice.get(choice_3)()


def update_customer():
    from tempfile import NamedTemporaryFile
    import shutil
    import csv
    search = input("Enter the customer Name")
    filename = '/home/intern/Desktop/Django/BMS/customer.csv'
    tempfile = NamedTemporaryFile(mode='w', delete=False)
    fields = ['Name', 'Email', 'Phone','Created_at','Status']
    with open(filename, 'r') as csvfile, tempfile:
        reader = csv.DictReader(csvfile, fieldnames=fields)
        writer = csv.DictWriter(tempfile, fieldnames=fields)
        for row in reader:
            if row['Name'] == search:
                print('updating row', row['Name'])
                row['Name'], row['Email'], row['Phone'],row['Status'] = input("Name"),
                input("Email"), 
                input("Phone"),
                input("Status")
            row = {'Name': row['Name'], 
            'Email': row['Email'], 
            'Phone': row['Phone'],
            'Created_at': row['Created_at'],
            'Status':row['Status']}
            writer.writerow(row)
    shutil.move(tempfile.name, filename)
                
def all_data():
    with open('/home/intern/Desktop/Django/BMS/customer.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)
def active_inactive():
    status = input("Enter active user or inactive user data you want options:- active/inactive enter-:")
    with open('/home/intern/Desktop/Django/BMS/customer.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Status'] == status:
                print(row)
            elif row['Status'] == status:
                print(row)
def check_valid_email(email):
    try:
      # validate and get info
        v = validate_email(email)
        # replace with normalized form
        # email = v["email"] 
        
    except EmailNotValidError as e:
        # email is not valid, exception message is human-readable form ma
        print(str(e))
        # return create_customer()


def subscription():
    print("**** MENU *******")
    print("Select the choice")
    choice_2=input('''
    Enter your choice
    1. Create Customer subcription
    2. Retrive Customer subcription
    3. Delete Customer subcription
    4. List Customer subcription
    5. Update customer subcription
    6. Exit 
    input:-''')
    choice={'1':create_customer_subscription,'2':retrive_customer_subscription,'3':delete_customer_subscription,'4':lis_customer_subscription,'5':update_customer_subscription,'6':exit}
    if choice_2 not in choice:
        print("Enter a valid input")
        subscription()
    choice.get(choice_2)()
    


def create_customer_subscription():
    customer_name = input("Enter Your Name:-")
    with open('/home/intern/Desktop/Django/BMS/customer.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for data in reader:
            if data['Name'] == customer_name: 
                email = data['Email']
                check_valid_email(email)
                from_date = date.today()
                status = input("Select the criteria paid or unpaid enter paid or unpaid:- ")
                if status == 'paid':
                    subscription_time = input('''Enter the subscription  option 
                type 
                1month
                6month
                1year
                input:-''')   
                    
                    subscription_tim ={'1month':{'amount':300,'to_date':from_date + datetime.timedelta(days=30)},
                    '6month':{'amount':1200,'to_date':from_date + datetime.timedelta(days=180)},
                    '1year':{'amount':2000,'to_date':from_date + datetime.timedelta(days=360)}}
                    amount_data=subscription_tim[subscription_time]['amount']
                    to_date_data=subscription_tim[subscription_time]['to_date']
                    
                else:
                    subscription_time=0
                    amount_data=0
                    to_date_data=0
                    print("You are not subscribed")
                # file_exists = os.path.isfile('subscription.csv')

                with open('/home/intern/Desktop/Django/BMS/subcription.csv', mode='a+') as csv_files:
                    fieldnames = ['customer_name','email', 'from_date', 'subscription_time','status','amount','to_date']
                    writer = csv.DictWriter(csv_files, fieldnames=fieldnames)
                    if  not  csv_files:
                        writer.writeheader()
                    writer.writerow({
                    'customer_name': customer_name,
                    'email':email, 
                    'from_date': from_date, 
                    'subscription_time':subscription_time,
                    'status':status,
                    'amount':amount_data,
                    'to_date':to_date_data
                    })
        subscription()
        print("Name does not match with registered customer")

def retrive_customer_subscription():
    search = input("Enter the customer Name:-")
    with open('/home/intern/Desktop/Django/BMS/subcription.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['customer_name'] == search:
                print(row)

def delete_customer_subscription():
    lines1 = [] 
    memberName = input("Please enter a member's name to be deleted:-")
    with open('/home/intern/Desktop/Django/BMS/subcription.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines1.append(row)
            for field in row:
                if field == memberName:
                    lines1.remove(row)
    with open('/home/intern/Desktop/Django/BMS/subcription.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines1)

def lis_customer_subscription():
    print("***list choices****")
    choice_3 = input('''choice any one
    1.All data
    2.Paid/Unpaid
    3.Exit
    input:-''')
    choice = {'1':all_subscription,'2':paid_unpaid,'3':exit}
    choice.get(choice_3)()
    

def update_customer_subscription():
    from tempfile import NamedTemporaryFile
    import shutil
    import csv
    search = input("Enter the subscriber Name")
    filename = '/home/intern/Desktop/Django/BMS/subcription.csv'
    tempfile = NamedTemporaryFile(mode='w', delete=False)
    fields = ['customer_name', 'from_date', 'subcription_time','status','amount','to_date']

    with open(filename, 'r') as csvfile, tempfile:
        reader = csv.DictReader(csvfile, fieldnames=fields)
        writer = csv.DictWriter(tempfile, fieldnames=fields)
        for row in reader:
            if row['customer_name'] == search:
                print('updating row', row['customer_name'])
                row['customer_name'], row['from_date'], row['subcription_time'],row['status'],row['amount'],row['to_date'] = input("customer_name"),input("from_date"),input("subcription_time"), input("status"),input("amount"),input("to_date")
            row = {'customer_name': row['customer_name'], 'from_date': row['from_date'], 'subcription_time': row['subcription_time'], 'status': row['status'],'amount':row['amount'],'to_date':row['to_date']}
            writer.writerow(row)
    shutil.move(tempfile.name, filename)


def all_subscription():
    with open('/home/intern/Desktop/Django/BMS/subcription.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)



def paid_unpaid():
    status = input("Enter paid or unpaid subcription  user data you want options:- paid/unpaid enter-:")
    with open('/home/intern/Desktop/Django/BMS/subcription.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['status'] == status:
                print(row)
            elif row['status'] == status:
                print(row)



def send_email():   
    with open('/home/intern/Desktop/Django/BMS/subcription.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:           
            from datetime import datetime
            if row['status'] == 'paid':
                d1=row['from_date']
                d2=row['to_date']
                startdate = datetime.strptime(d1, '%Y-%m-%d').date()
                enddate = datetime.strptime(d2, '%Y-%m-%d').date()
                result=enddate-startdate
                subtractdate=result.days
                print(subtractdate)
            
                if subtractdate <= 5 and row['status']=='paid':
                    
                    email_sender='074bex006.lalit@sagarmatha.edu.np'
                    email_password='yybjkbusiqtabkqo'
                    email_receiver=row['email']

                    subject="Subscription time is going to timeout!!!"
                    body=""""
            Your subscripton is running out so please buy subscription at timely.
            Thank You!!!


            """      
                    em=EmailMessage()
                    em['from']=email_sender
                    em['to']=email_receiver
                    em['subject']=subject
                    em.set_content(body)
                    context=ssl.create_default_context()
                    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
                        smtp.login(email_sender,email_password)
                        smtp.sendmail(email_sender,email_receiver,em.as_string())
                    print("Congratulation your mail is send!!")
choose()
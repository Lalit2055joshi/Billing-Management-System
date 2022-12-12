import datetime
print("******Menu********")
choice = input('''
Enter your Choice
1.Customer 
2.Subscription
3.Exit
''')

def choose(choice):
    
    if choice == 1:
        customer()    
    # elif choice == 2:2
    #     subscription()
    elif choice == 3:
        print("Thanks for serving us")
        exit()
    else:
        print("Enter valid number")
        choose()
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
    ''')
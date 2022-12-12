class BillingMS:
    print("******Menu********")
    def __init__(self,choice):
        self.choice = choice
    
    def customer(self):
        pass
    
    def choose(self):
        print("Choice any one 1 2 or 3")
        if self.choice == 1:
            
        elif self.choice == 2:
            subscription()
        elif self.choice == 3:
            print("Thanks for serving us")
            break
            
    
    def subscription(self):
        pass
     


choice = input("Enter your Choice")
BillingMS(choice)
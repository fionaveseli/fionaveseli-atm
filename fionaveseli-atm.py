class bankAccount():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self):
        amount = float(input(f"You currently have {self.balance}$ in your account. Enter the amount you want to deposit: "))
        self.balance = self.balance + amount
        if (amount >= 0):
            print(f"Deposit is successful\nYour balance is now {self.balance}$")
            return True
        else:
            print("You can deposit any value greater than zero")
            return False


    def withdraw(self):
        amount = float(input(f"You currently have {self.balance}$ in your account. Enter the amount of money you to withdraw: "))
        if (amount <= self.balance):
            self.balance = self.balance - amount
            print(f"Deposit is successful \nYour balance is now {self.balance}$")
        else: 
            print(f"You can't withdraw more than your amount in account \nYour balance is {self.balance}$")

    def Balance(self):
        print(f"Your Balance is {self.balance}$")
    
    def login(self):
        user_name = input("What is your name? ")
        print(f"Hello {user_name}! Welcome to RITK ATM " )
        pin = input(f"Please enter your card pin here: ")
        while( pin != "123456"):
            pin = input("Login failed! Please enter your CORRECT password: ")            
        else:
            self.start()
    
    def start(self):
        while True: 
            print("1 - Deposit")
            print("2 - Withdraw")
            print("3 - Balance")
            print("4 - Log Out")
            choice = input("Please choose your desired transaction: ")
            if choice == "1":
                self.deposit()
                new = input("Do you want to make another transaction? Type 'yes' if you do, and 'no' if you don't.\n ")
                if new == "yes":
                    continue
                if new == "no":
                    print("Thank you for using RITK ATM Machine! ")
                    break
            elif choice == "2":
                self.withdraw()
                new = input("Do you want to make another transaction? Type 'yes' if you do, and 'no' if you don't.\n ")
                if new == "yes":
                    continue
                if new == "no":
                    print("Thank you for using RITK ATM Machine! ")
                    break                
            if choice ==  "3":
                self.Balance()           
                new = input("Do you want to make another transaction? Type 'yes' if you do, and 'no' if you don't.\n ")
                if new == "yes":
                    continue
                if new == "no":
                    print("Thank you for using RITK ATM Machine! ")
                    break 
            elif choice == "4":
                print("You have logged out of your account!")
                break
            else: 
                print("Please use one of the options provided to you")

account = bankAccount("Fiona", 1500)
account.login()

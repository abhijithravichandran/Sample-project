class ATM():
    def __init__(self,name,balance):
        
        self.balance = balance
        self.name = name
    

    def debit(self,amount_debited):
        self.balance = self.balance + float(amount_debited)
    def withdraw(self,amount_withdraw):
        self.withdraw -= amount_withdraw
    
    def display_balance(self):
        print(f"The balance of {self.name} is {self.balance:.2f}")

name = input("Enter the name")
balance = float(input("Enter the balance"))
customber1 = ATM(name,balance)

choice = ""
while(choice.lower() != "done"):
    choice = input("If you want to credit or withdraw or check balance or 'done':")   
    if choice.lower() == "credit":
        debit = float(input("Enter a amount to debit"))
        customber1.debit(debit)
    elif (choice.lower() == "withdraw"):
        withdraw = float(input("Enter amount to withdraw"))
        customber1.withdraw(withdraw)
    elif (choice.lower() == "balance"):
        customber1.display_balance()


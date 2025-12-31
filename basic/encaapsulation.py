# create a class bank  with 2 att balance and accout number
# create methods to deposit withdraw and display balance
import random 



class bank:
    def __init__(self,balance=0):
        self.__account_number=random.randint(1000000,99999999)
        self.__balance=balance

    def credit(self,amount):
        self.__balance+=amount
        print(f"Credited  {amount} to account {self.__account_number}")

    def debit(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print(f"Withdrew {amount} from account {self.__account_number}")
        else:
            print("Insufficient balance")

    def display_balance(self):
        print(f"Account {self.__account_number} has a balance of {self.__balance}")

# Usage
my_bank=bank(1000)      
my_bank.display_balance()
my_bank.credit(500)
my_bank.display_balance()
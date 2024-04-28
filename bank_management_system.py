import random
from datetime import datetime

class Bank:
    total_loan_amount = 0
    accounts = {}
    def __init__(self):
        self.loan_limit = 2
        self.bankrupt = False
        self.loan_feature_enabled = True 

    def create_account(self, name, email, address, account_type):
        account_number = random.randint(100000, 999999)
        self.accounts[account_number] = {
            "name": name,
            "email": email,
            "address": address,
            "account_type": account_type,
            "balance": 0,  
            "transactions": [],  
            "loan_count": 0
        }
        print(f"Mr.{name}, Your account has been successfully created. Your account number is: {account_number}")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number]["balance"] += amount
            self.accounts[account_number]["transactions"].append(f"Transaction no: {random.randint(10000, 80000)}, Deposited {amount}, datetime: {datetime.now()}")
            print(f"{amount} deposited successfully")
        else:
            print("Account does not exist")

    def check_balance(self, account_number):
        if account_number in self.accounts:
            print(f"Your current balance is: {self.accounts[account_number]['balance']}")
        else:
            print("Invalid account")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if not self.bankrupt:
                if amount <= self.accounts[account_number]["balance"]:
                    self.accounts[account_number]["balance"] -= amount
                    self.accounts[account_number]["transactions"].append(f"Transaction no: {random.randint(10000, 80000)}, Withdraw {amount}, datetime: {datetime.now()}")
                    print(f"{amount} withdrawn successfully")
                else:
                    print("Invalid withdrawal amount")
            else:
                print("The bank is bankrupt")
        else:
            print("Account does not exist")

    def check_transaction_history(self, account_number):
        if account_number in self.accounts:
            print(self.accounts[account_number]["transactions"])
        else:
            print("Account does not exist")

    def take_loan(self, account_number, amount):
        if account_number in self.accounts and not self.bankrupt and self.loan_feature_enabled:
            if self.accounts[account_number]["loan_count"] < self.loan_limit:
                    self.accounts[account_number]["balance"] += amount
                    self.total_loan_amount += amount
                    self.accounts[account_number]["transactions"].append(f"Transaction no: {random.randint(10000, 80000)}, Took loan {amount}, datetime: {datetime.now()}")
                    self.accounts[account_number]["loan_count"] += 1
                    print(f"{amount} loan successful")
            else:
                print("Maximum loan limit reached")
        elif not self.loan_feature_enabled:
            print("The loan feature is currently disabled.")
        else:
            print("Account does not exist")

    def fund_transfer(self, account_number, receiver_acc_number, amount):
        if account_number in self.accounts:
            if receiver_acc_number in self.accounts:
                if amount <= self.accounts[account_number]["balance"] and amount >= 0:
                    self.accounts[account_number]["balance"] -= amount
                    self.accounts[receiver_acc_number]["balance"] += amount
                    print(f"{amount} transfer successful")
                else:
                    print("Invalid transfer amount or insufficient balance")
            else:
                print("Receiver account does not exist")
        else:
            print("Sender account does not exist")

    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print("Account deleted successfully")
        else:
            print("Account does not exist")

    def toggle_loan_feature(self, status):
        self.loan_feature_enabled = status
        print("Loan feature is now", "enabled" if status else "disabled")

    def toggle_bankrupt_status(self, status):
        self.bankrupt = status
        print("Bankrupt status is now", "enabled" if status else "disabled")


class Admin:
    def __init__(self, name, email, bank_instance):
        self.name = name
        self.email = email
        self.bank = bank_instance

    def create_account(self, name, email, address, account_type):
        self.bank.create_account(name, email, address, account_type)

    def delete_account(self, account_number):
        self.bank.delete_account(account_number)
    
    def see_all_user_accounts(self):
        for account_number, account_info in self.bank.accounts.items():
            print(f"Account Number: {account_number}")
            print(f"Name: {account_info['name']}")
            print(f"Email: {account_info['email']}")
            print(f"Address: {account_info['address']}")
            print(f"Account Type: {account_info['account_type']}")
            print(f"Balance: {account_info['balance']}")
            print("------------------------")

    def check_total_loan_amount(self):
        print(f"Total loan amount is: {self.bank.total_loan_amount}")

    def total_available_balance(self):
        print(f"Total available balance is: {sum(acc['balance'] for acc in self.bank.accounts.values())}")

    def toggle_loan_feature(self, status):
        self.bank.toggle_loan_feature(status)

    def change_bankrupt_status(self, status):
        self.bank.toggle_bankrupt_status(status)


class User:
    def __init__(self, bank_instance):
        self.bank = bank_instance

    def create_account(self, name, email, address, account_type):
        self.bank.create_account(name, email, address, account_type)

    def deposit(self, account_number, amount):
        self.bank.deposit(account_number, amount)

    def withdraw(self, account_number, amount):
        self.bank.withdraw(account_number, amount)

    def check_balance(self, account_number):
        self.bank.check_balance(account_number)

    def see_transaction(self, account_number):
        self.bank.check_transaction_history(account_number)

    def fund_transfer(self, account_number, receiver_acc_number, amount):
        self.bank.fund_transfer(account_number, receiver_acc_number, amount)

    def take_loan(self, account_number, amount):
        self.bank.take_loan(account_number, amount)


def user_menu(bank_instance):
    U = User(bank_instance)
    while True:
        print("Option\n")
        print("1. Create account")
        print("2. Deposit")
        print("3. Check Balance")
        print("4. Check transaction history")
        print("5. Fund transfer")
        print("6. Withdraw")
        print("7. Take loan")
        print("8. Exit")
        choice = int(input("Enter the option: "))
        if choice == 1:
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            address = input("Enter your address: ")
            account_type = input("Enter your account_type: ")
            U.create_account(name, email, address, account_type)
        elif choice == 2:
            account_number = int(input("Enter account Number: "))
            amount = int(input("Enter amount: "))
            U.deposit(account_number, amount)
        elif choice == 3:
            account_number = int(input("Enter account Number: "))
            U.check_balance(account_number)
        elif choice == 4:
            account_number = int(input("Enter account Number: "))
            U.see_transaction(account_number)
        elif choice == 5:
            account_number = int(input("Enter account Number: "))
            receiver_acc = int(input("Enter receiver account number: "))
            amount = int(input("Enter amount: "))
            U.fund_transfer(account_number, receiver_acc, amount)
        elif choice == 6:
            account_number = int(input("Enter account Number: "))
            amount = int(input("Enter amount: "))
            U.withdraw(account_number, amount)
        elif choice == 7:
            account_number = int(input("Enter account Number: "))
            amount = int(input("Enter amount: "))
            U.take_loan(account_number, amount)
        elif choice == 8:
            break
        else:
            print("Invalid input, try again")


def admin_menu(bank_instance):
    name = input("Enter admin name: ")
    email = input("Enter admin email: ")
    A = Admin(name, email, bank_instance) 
    while True:
        print("Option\n")
        print("1. Create account")
        print("2. Delete account")
        print("3. All user accounts")
        print("4. Total available balance")
        print("5. Total loan amount")
        print("6. Change Loan feature")
        print("7. Change Bankrupt status")
        print("8. Exit")
        choice = int(input("Enter the option: "))
        if choice == 1:
            name = input("Enter name: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            account_type = input("Enter account_type: ")
            A.create_account(name, email, address, account_type)
        elif choice == 2:
            account_number = int(input("Enter account Number: "))
            A.delete_account(account_number)
        elif choice == 3:
            A.see_all_user_accounts()
        elif choice == 4:
            A.total_available_balance()
        elif choice == 5:
            A.check_total_loan_amount()
        elif choice == 6:
            status = input("Enter 'on' to enable or 'off' to disable loan feature: ").lower()
            if status == 'on':
                A.toggle_loan_feature(True)
            elif status == 'off':
                A.toggle_loan_feature(False)
            else:
                print("Invalid input")
        elif choice == 7:
            status = input("Enter 'on' to enable or 'off' to disable bankrupt status: ").lower()
            if status == 'on':
                A.change_bankrupt_status(True)
            elif status == 'off':
                A.change_bankrupt_status(False)
            else:
                print("Invalid input")
        elif choice == 8:
            break
        else:
            print("Invalid input, try again")

bank_instance = Bank()
while True:
    print("Option\n")
    print("1. User")
    print("2. Admin")
    print("3. Exit")
    choice = int(input("Enter option: "))
    if choice == 1:
        user_menu(bank_instance)
    elif choice == 2:
        admin_menu(bank_instance)
    elif choice == 3:
        break
    else:
        print("Invalid option, try again")

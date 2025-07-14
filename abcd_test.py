import os
import time
from datetime import datetime

class ATM:
    def __init__(self):
        self.users = {
            '12345': {
                'pin': '1234',
                'balance': 1000.0,
                'name': 'John Doe',
                'transactions': []
            }
        }
        self.current_user = None
        self.account_number = None

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def log_transaction(self, transaction_type, amount=None):
        if self.current_user:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            transaction = {
                'type': transaction_type,
                'amount': amount,
                'timestamp': timestamp,
                'balance': self.users[self.account_number]['balance']
            }
            self.users[self.account_number]['transactions'].append(transaction)

    def login(self):
        self.clear_screen()
        print("=== ATM Login ===")
        self.account_number = input("Enter account number: ")
        pin = input("Enter PIN: ")

        if self.account_number in self.users and self.users[self.account_number]['pin'] == pin:
            self.current_user = self.users[self.account_number]
            return True
        return False

    def check_balance(self):
        self.clear_screen()
        print(f"Current Balance: ${self.current_user['balance']:.2f}")
        self.log_transaction('balance_check')
        time.sleep(2)

    def withdraw(self):
        self.clear_screen()
        print("=== Withdraw Money ===")
        amount = float(input("Enter amount to withdraw: $"))
        
        if amount > self.current_user['balance']:
            print("Insufficient funds!")
        elif amount <= 0:
            print("Invalid amount!")
        else:
            self.current_user['balance'] -= amount
            self.log_transaction('withdrawal', amount)
            print(f"Successfully withdrew ${amount:.2f}")
            print(f"New balance: ${self.current_user['balance']:.2f}")
        time.sleep(2)

    def deposit(self):
        self.clear_screen()
        print("=== Deposit Money ===")
        amount = float(input("Enter amount to deposit: $"))
        
        if amount <= 0:
            print("Invalid amount!")
        else:
            self.current_user['balance'] += amount
            self.log_transaction('deposit', amount)
            print(f"Successfully deposited ${amount:.2f}")
            print(f"New balance: ${self.current_user['balance']:.2f}")
        time.sleep(2)

    def change_pin(self):
        self.clear_screen()
        print("=== Change PIN ===")
        current_pin = input("Enter current PIN: ")
        if current_pin == self.current_user['pin']:
            new_pin = input("Enter new PIN (4 digits): ")
            if len(new_pin) == 4 and new_pin.isdigit():
                self.current_user['pin'] = new_pin
                self.log_transaction('pin_change')
                print("PIN successfully changed!")
            else:
                print("Invalid PIN format!")
        else:
            print("Incorrect current PIN!")
        time.sleep(2)

    def show_mini_statement(self):
        self.clear_screen()
        print("=== Mini Statement ===")
        print(f"Account Holder: {self.current_user['name']}")
        print("\nRecent Transactions:")
        for transaction in self.current_user['transactions'][-5:]:
            print(f"Type: {transaction['type']}")
            if transaction['amount']:
                print(f"Amount: ${transaction['amount']:.2f}")
            print(f"Date: {transaction['timestamp']}")
            print(f"Balance: ${transaction['balance']:.2f}")
            print("-" * 30)
        input("Press Enter to continue...")

    def run(self):
        while True:
            if not self.current_user:
                if not self.login():
                    print("Invalid credentials!")
                    time.sleep(1)
                    continue

            self.clear_screen()
            print("\n=== ATM Menu ===")
            print("1. Check Balance")
            print("2. Withdraw Money")
            print("3. Deposit Money")
            print("4. Change PIN")
            print("5. Mini Statement")
            print("6. Logout")
            print("7. Exit")

            choice = input("\nEnter your choice (1-7): ")

            if choice == '1':
                self.check_balance()
            elif choice == '2':
                self.withdraw()
            elif choice == '3':
                self.deposit()
            elif choice == '4':
                self.change_pin()
            elif choice == '5':
                self.show_mini_statement()
            elif choice == '6':
                self.current_user = None
                self.account_number = None
                print("Logged out successfully!")
                time.sleep(1)
            elif choice == '7':
                print("Thank you for using our ATM. Goodbye!")
                break
            else:
                print("Invalid choice!")
                time.sleep(1)

if __name__ == "__main__":
    atm = ATM()
    atm.run()
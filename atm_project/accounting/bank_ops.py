from utils import create_user_file


class BankOperation:
    def __init__(self, current_balance=100):
        self.current_balance = current_balance
        self.bank_account = ""
        self.card_number = ""
        self.bank_account_initial_no = "145"
        self.bank_branch = "001"
        self.card_reference = "999"

    def create_account(self, first_name, last_name, email):
        self.bank_account = self.create_bank_account()
        self.card_number = self.create_card_no()
        user_data = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "bank_account": self.bank_account,
            "card_number": self.card_number,
            "current_balance": self.current_balance
        }

        create_user_file(f"{self.card_number}.txt", user_data)
        print("Account Created Successfully")
        print(f"Your bank account number is {self.bank_account}")
        print(f"Your card number is {self.card_number}")

    def create_bank_account(self):
        bank_account_no = f"{self.bank_account_initial_no}{self.bank_branch}001"
        return bank_account_no

    def create_card_no(self):
        card_no = f"{self.bank_account_initial_no}{self.bank_branch}{self.card_reference}001"
        return card_no

    def withdraw_amount(self, withdraw_amount: int, user_data: dict):
        if withdraw_amount > user_data['current_balance']:
            print("Insufficient Balance")
            return
        user_data['current_balance'] -= withdraw_amount
        create_user_file(f"{user_data['card_number']}.txt", user_data)
        print(f"Amount {withdraw_amount} withdrawn successfully")
        print(f"Current balance is {user_data['current_balance']}")

    def diposit_amount(self, diposit_amount:int, user_data: dict):
        if diposit_amount <= 0:
            print("Invalid diposit amount")
            return
        user_data['current_balance'] += diposit_amount
        create_user_file(f"{user_data['card_number']}.txt", user_data)
        print(f"Amount {diposit_amount} withdrawn successfully")
        print(f"Current balance is {user_data['current_balance']}")

    def check_balance(self, user_data: dict):
        print(f"Your current balance is {user_data['current_balance']}")
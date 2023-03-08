"""
1. User Create
    # Make a separate folder for user operation
    # Make a different module for different type user operation

2. ATM Operation
    # Check the card no and pin
    # Ask withdraw amount and check user balance
    # Make decision based on balance
"""
from accounting.bank_ops import BankOperation
from utils import get_user_data


def main():
    print("Welcome to ATM System.")
    print("""
        1. Create an Account
        2. ATM Operation
        3. Exit
    """)
    choice = int(input("Enter Your Choice:"))

    if choice == 1:
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        email = input("Enter your email: ")
        current_balance = int(input("Enter your balance: "))
        if current_balance < 100:
            print("You need to have minimum 100 balance")
            return

        BankOperation(current_balance).create_account(first_name, last_name, email)


    elif choice == 2:
        card_number = input("Enter your card number: ")
        user_data = get_user_data(f"{card_number}.txt")
        if not user_data:
            print("Invalid Card Number.")
            return

        print(f"Welcome {user_data['first_name']} to ATM System.")

        while True:
            print("""
                    1. Withdraw
                    2. Deposit
                    3. Check Balance
                    4. Exit
                """)
            atm_choice = int(input("Enter Your Choice: "))
            if atm_choice == 1:
                withdraw_amount = int(input("Enter withdraw amount: "))
                BankOperation().withdraw_amount(withdraw_amount, user_data)
            elif atm_choice == 2:
                deposit_amount = int(input("Enter deposit amount: "))
                BankOperation().diposit_amount(deposit_amount, user_data)
            elif atm_choice == 3:
                BankOperation().check_balance(user_data)
            elif atm_choice == 4:
                print("Thank you for using our ATM system ")
                return
            else:
                print("Invalid ATM Choice")
                return
    elif choice == 3:
        # exit()
        return
    else:
        print("Invalid operation")


main()

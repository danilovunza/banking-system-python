"""
Banking System

Author: Danilo Vunza
Course: COSC 1437

Description:
A banking system developed using
Object-Oriented Programming concepts.
"""


class Transaction:

    def __init__(
        self,
        transaction_type,
        amount,
        description
    ):

        self.transaction_type = transaction_type
        self.amount = amount
        self.description = description

    def __str__(self):

        return (
            f"{self.transaction_type} | "
            f"${self.amount:.2f} | "
            f"{self.description}"
        )


class Customer:

    def __init__(
        self,
        customer_id,
        name
    ):

        self.customer_id = customer_id
        self.name = name


class Account:

    def __init__(
        self,
        account_number,
        owner
    ):

        self.account_number = account_number
        self.owner = owner

        self.balance = 0.0

        self.transactions = []

    def deposit(self, amount):

        self.balance += amount

        self.transactions.append(
            Transaction(
                "Deposit",
                amount,
                "Money deposited"
            )
        )

    def withdraw(self, amount):

        if amount > self.balance:

            return False

        self.balance -= amount

        self.transactions.append(
            Transaction(
                "Withdrawal",
                amount,
                "Money withdrawn"
            )
        )

        return True

    def show_history(self):

        print("\nTRANSACTION HISTORY")

        print("-" * 50)

        if len(self.transactions) == 0:

            print("No transactions found.")

            return

        for transaction in self.transactions:

            print(transaction)


class Bank:

    def __init__(self):

        self.accounts = {}

    def create_account(
        self,
        account_number,
        customer_name
    ):

        customer = Customer(
            account_number,
            customer_name
        )

        account = Account(
            account_number,
            customer
        )

        self.accounts[
            account_number
        ] = account

        print(
            "\nAccount created successfully."
        )

    def get_account(
        self,
        account_number
    ):

        return self.accounts.get(
            account_number
        )

    def transfer(
        self,
        sender_account,
        receiver_account,
        amount
    ):

        sender = self.get_account(
            sender_account
        )

        receiver = self.get_account(
            receiver_account
        )

        if sender is None or receiver is None:

            print(
                "\nInvalid account."
            )

            return

        if sender.withdraw(amount):

            receiver.deposit(amount)

            sender.transactions.append(
                Transaction(
                    "Transfer Out",
                    amount,
                    f"To {receiver_account}"
                )
            )

            receiver.transactions.append(
                Transaction(
                    "Transfer In",
                    amount,
                    f"From {sender_account}"
                )
            )

            print(
                "\nTransfer completed."
            )

        else:

            print(
                "\nInsufficient funds."
            )


def display_menu():

    print("\n" + "=" * 50)

    print("BANKING SYSTEM")

    print("=" * 50)

    print("1. Create Account")

    print("2. Deposit")

    print("3. Withdraw")

    print("4. Transfer")

    print("5. View Account")

    print("6. Transaction History")

    print("7. Exit")

    print("=" * 50)


def main():

    bank = Bank()

    while True:

        display_menu()

        choice = input(
            "Select an option: "
        )

        if choice == "1":

            account_number = input(
                "Account Number: "
            )

            name = input(
                "Customer Name: "
            )

            bank.create_account(
                account_number,
                name
            )

        elif choice == "2":

            account_number = input(
                "Account Number: "
            )

            account = bank.get_account(
                account_number
            )

            if account:

                amount = float(
                    input(
                        "Deposit Amount: $"
                    )
                )

                account.deposit(amount)

                print(
                    "Deposit successful."
                )

            else:

                print(
                    "Account not found."
                )

        elif choice == "3":

            account_number = input(
                "Account Number: "
            )

            account = bank.get_account(
                account_number
            )

            if account:

                amount = float(
                    input(
                        "Withdraw Amount: $"
                    )
                )

                if account.withdraw(amount):

                    print(
                        "Withdrawal successful."
                    )

                else:

                    print(
                        "Insufficient funds."
                    )

            else:

                print(
                    "Account not found."
                )

        elif choice == "4":

            sender = input(
                "Sender Account: "
            )

            receiver = input(
                "Receiver Account: "
            )

            amount = float(
                input(
                    "Transfer Amount: $"
                )
            )

            bank.transfer(
                sender,
                receiver,
                amount
            )

        elif choice == "5":

            account_number = input(
                "Account Number: "
            )

            account = bank.get_account(
                account_number
            )

            if account:

                print(
                    f"\nOwner: "
                    f"{account.owner.name}"
                )

                print(
                    f"Account: "
                    f"{account.account_number}"
                )

                print(
                    f"Balance: "
                    f"${account.balance:.2f}"
                )

            else:

                print(
                    "Account not found."
                )

        elif choice == "6":

            account_number = input(
                "Account Number: "
            )

            account = bank.get_account(
                account_number
            )

            if account:

                account.show_history()

            else:

                print(
                    "Account not found."
                )

        elif choice == "7":

            print(
                "\nThank you for using the Banking System."
            )

            break

        else:

            print(
                "\nInvalid option."
            )


main()

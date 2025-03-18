class ATM:
    def __init__(self):
        self.balance = 0
        self.pin = "1234"  # Default PIN
        self.transaction_history = []

    def authenticate(self):
        # Authenticate user by PIN
        entered_pin = input("Enter PIN: ")
        if entered_pin == self.pin:
            return True
        else:
            print("Incorrect PIN.")
            return False

    def balance_inquiry(self):
        # Display account balance
        print(f"Your current balance is: ${self.balance}")

    def cash_withdrawal(self):
        # Withdraw cash from account
        amount = float(input("Enter amount to withdraw: $"))
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount}")
            print(f"Withdrawal successful! Your new balance is ${self.balance}.")
        else:
            print("Insufficient funds.")

    def cash_deposit(self):
        # Deposit cash into account
        amount = float(input("Enter amount to deposit: $"))
        self.balance += amount
        self.transaction_history.append(f"Deposited: ${amount}")
        print(f"Deposit successful! Your new balance is ${self.balance}.")

    def change_pin(self):
        # Change account PIN
        current_pin = input("Enter current PIN: ")
        if current_pin == self.pin:
            new_pin = input("Enter new PIN: ")
            self.pin = new_pin
            print("PIN changed successfully.")
        else:
            print("Incorrect PIN.")

    def transaction_history_view(self):
        # View transaction history
        if not self.transaction_history:
            print("No transaction history available.")
        else:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)

    def menu(self):
        while True:
            print("\nATM Menu:")
            print("1. Balance Inquiry")
            print("2. Cash Withdrawal")
            print("3. Cash Deposit")
            print("4. Change PIN")
            print("5. View Transaction History")
            print("6. Exit")

            choice = input("Please select an option (1-6): ")

            if choice == "1":
                self.balance_inquiry()
            elif choice == "2":
                self.cash_withdrawal()
            elif choice == "3":
                self.cash_deposit()
            elif choice == "4":
                self.change_pin()
            elif choice == "5":
                self.transaction_history_view()
            elif choice == "6":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    atm = ATM()
    
    if atm.authenticate():
        atm.menu()
    else:
        print("Authentication failed. Exiting ATM.")

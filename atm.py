class ATM:
    def __init__(self):
        self.balance = 0
        self.pin = None
        self.logged_in = False

    def login(self):
        pin = input("Enter your PIN: ")
        # Check if the PIN is correct (you can customize this part)
        if pin == "0963":
            print("Login successful!")
            self.logged_in = True
        else:
            print("Invalid PIN. Login failed.")

    def logout(self):
        self.logged_in = False
        print("Logged out successfully.")

    def check_balance(self):
        if self.logged_in:
            print(f"Your balance is {self.balance} dollars.")
        else:
            print("Please log in first.")

    def deposit(self):
        if self.logged_in:
            amount = float(input("Enter the amount to deposit: "))
            self.balance += amount
            print(f"{amount} dollars deposited successfully.")
        else:
            print("Please log in first.")

    def withdraw(self):
        if self.logged_in:
            amount = float(input("Enter the amount to withdraw: "))
            if amount > self.balance:
                print("Insufficient balance.")
            else:
                self.balance -= amount
                print(f"{amount} dollars withdrawn successfully.")
        else:
            print("Please log in first.")


def main():
    atm = ATM()

    while True:
        print("\n===== MGX ATM Simulator =====")
        print("1. Login")
        print("2. Logout")
        print("3. Check Balance")
        print("4. Deposit")
        print("5. Withdraw")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            atm.login()
        elif choice == "2":
            atm.logout()
        elif choice == "3":
            atm.check_balance()
        elif choice == "4":
            atm.deposit()
        elif choice == "5":
            atm.withdraw()
        elif choice == "6":
            print("Thank you for using the MGX ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

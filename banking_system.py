# Dictionary to store accounts and balances
accounts = {}
4
# Function to create a new account
def create_account():
    account_number = input("Enter a new account number: ")
    if account_number in accounts:
        print("Account already exists!")
    else:
        name = input("Enter account holder's name: ")
        balance = float(input("Enter initial balance: "))
        accounts[account_number] = {"name": name, "balance": balance}
        print(f"Account created successfully for {name}!")

# Function to deposit money
def deposit():
    account_number = input("Enter your account number: ")
    if account_number in accounts:
        amount = float(input("Enter the amount to deposit: "))
        if amount > 0:
            accounts[account_number]["balance"] += amount
            print(f"Deposited {amount}. New balance: {accounts[account_number]['balance']}")
        else:
            print("Invalid amount!")
    else:
        print("Account not found!")

# Function to withdraw money
def withdraw():
    account_number = input("Enter your account number: ")
    if account_number in accounts:
        amount = float(input("Enter the amount to withdraw: "))
        if amount > 0 and amount <= accounts[account_number]["balance"]:
            accounts[account_number]["balance"] -= amount
            print(f"Withdrew {amount}. New balance: {accounts[account_number]['balance']}")
        else:
            print("Insufficient funds or invalid amount!")
    else:
        print("Account not found!")

# Function to check balance
def check_balance():
    account_number = input("Enter your account number: ")
    if account_number in accounts:
        print(f"Account balance for {accounts[account_number]['name']}: {accounts[account_number]['balance']}")
    else:
        print("Account not found!")

# Function to transfer money
def transfer_money():
    from_account = input("Enter your account number: ")
    to_account = input("Enter the recipient's account number: ")
    if from_account in accounts and to_account in accounts:
        amount = float(input("Enter the amount to transfer: "))
        if amount > 0 and amount <= accounts[from_account]["balance"]:
            accounts[from_account]["balance"] -= amount
            accounts[to_account]["balance"] += amount
            print(f"Transferred {amount} to {accounts[to_account]['name']}.")
        else:
            print("Insufficient funds or invalid amount!")
    else:
        print("One or both accounts not found!")

# Main menu
def main():
    while True:
        print("\nSIMPLE BANKING SYSTEM")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Transfer Money")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            transfer_money()
        elif choice == "6":
            print("Thank you for using the Simple Banking System. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the program
if __name__ == "__main__":
    main()

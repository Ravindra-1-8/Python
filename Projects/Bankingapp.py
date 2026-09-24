balance = 0.0
transaction_history = []

def deposit(amount):
    global balance
    
    balance += amount
    transaction_history.append(f"Deposited: {amount}/-")
    print(f"{amount}/- deposited successfully.\n")
    
def withdraw(amount):
    global balance
    
    if amount > balance:
        print("Sorry! Insufficient balance.\n")
    else:
        balance -= amount
        transaction_history.appent(f"Withdrew:{amount}/-")
        print(f"{amount}/- withdrawn successfully.\n")
        
def check_balance():
    print(f"Current balance: {balance}\n")
    
    
def view_transaction_history():
    
    if not transaction_history:
        print("No transcations yet\n")
    else:
        print("---------Transaction History---------")
        
        for t in transaction_history:
            print("\n-",t)
            
        deposit = sum(1 for t in transaction_history if "Deposit" in t)
        withdraw = sum(1 for t in transaction_history if "Withdraw" in t)
        print(f"\n Total deposits: {deposit}")
        print(f"Total withdrawals: {withdraw}\n")
        
def menu():
    
    while True:
        print("Welcome to the Banking App")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. View Transaction History")
        print("5. Exit")
        
        choice = input("Enter your choice: \n")
        
        if choice == '1':
            amount = float(input("Enter amount to deposit:\n"))
            deposit(amount)
            
        elif choice == '2':
            amount = float(input("Enter amount to withdraw:\n"))
            withdraw(amount)
            
        elif choice == '3':
            check_balance()
            
        elif choice == '4':
            view_transaction_history()
            
        elif choice == '5':
            print("Thank you for using the Banking App. Goodbye!")
            break
        
        else:
            print("Sorry! Please enter a valid choice.")
            
menu()
        
def show_balance(balance):
    print(float(balance))

def deposit(balance):
    amount = input("Enter amount to deposit: ")
    return balance + int(amount)

def withdraw(balance):
    amount = input("Enter amount to withdraw: ")
    return balance - int(amount)

def logout(name):
    print("Goodbye", name + "!")

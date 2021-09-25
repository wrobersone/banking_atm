from banking_pkg import account
def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

print("          === Automated Teller Machine ===          ")
print("LOGIN")
name = input("Enter name: ")
pin = input("Enter PIN: ")
balance = 0  
print(f"{name} has been registered with the starting balance of ${balance}")

while True:
    name_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter PIN: ")
    
    if name == name_to_validate and pin == pin_to_validate:
                
        print("Login successful!")
        break
    print("Invalid credentials!")
        
while True:
    atm_menu(name)
    option = input("Choose an option: ")
    if option == "1":
        account.show_balance(balance)
    if option == "2":
        balance = account.deposit(balance)
    if option == "3":
        balance = account.withdraw(balance)
    if option == "4":
        account.logout(name)
        break

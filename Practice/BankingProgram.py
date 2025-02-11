#Python Banking Program

def show_balance(balance):
    print(f"Your balance is Rs. {balance:.2f}")

def deposit():
    is_Valid=False
    while not is_Valid:
        amount=float(input("Enter an amount to be deposited: "))

        if amount<0:
            print("Thats not a valid amount")
        else:
            is_Valis=True
            return amount

def withdraw(balance):
    is_Enough = False
    while not is_Enough:
        amount=float(input("Enter amount to be withdrawn: "))
        if amount>balance:
            print("Insufficient funds")
        elif amount<0:
            print("Amount must be greater than 0")
        else:
            is_Enough=True
            return amount

def main():

    balance=0
    is_running=True

    while is_running:
        print("Banking Program")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")

        choice=input("Enter your choice (1-4): ")
        if choice == '1':
            show_balance(balance)
        elif choice=='2':
            balance+=deposit()
        elif choice=='3':
            balance-=withdraw(balance)
        elif choice=='4' or choice=="":
            is_running=False
        else:
            print()
            print("Enter Valid Choice")


if __name__=='__main__':
    main()
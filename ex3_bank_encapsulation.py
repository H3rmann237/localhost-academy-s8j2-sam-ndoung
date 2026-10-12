class BankAccount :
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self) :
        return self.__balance

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Montant invalide.")

    def withdraw(self,amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Retrait impossible")

account = BankAccount("Alice",1000)

print (account.balance)

account.deposit(500)
print(account.balance)

account.withdraw(300)
print(account.balance)

account.withdraw(5000)
print(account.balance)
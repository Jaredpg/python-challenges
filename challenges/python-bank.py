class bank_account:
    def __init__(self, value, interest_rate, compound_interest, year):
        self.value = value
        self.year = year
        self.compound_interest = compound_interest
        self.interest_rate = interest_rate 

    def interest_rate(self, interest_rate):
        interest = self.value * 1.3 
        print(interest_rate)

    def withdraw(self, amount):
        self.value -= amount
        print("you withdrawed £" + str(amount) + " you now have £" + str(self.value)) 

    def deposit(self, amount):
        self.value += amount
        print("you deposited £" + str(amount) + " you now have £" + str(self.value))

    def total(self): 
        print("your total is: £" + str(self.value))
    
    def increment_year(self):
        if self.compound_interest:
            self.value *= self.interest_rate 
        else:
            self.value += self.interest_rate
        self.year += 1
        print("increment year: " + str(self.year))
            
myBank = bank_account(20, 1.3, False, 2023)

myBank.deposit(8)
myBank.withdraw(5)
myBank.increment_year()
myBank.total()


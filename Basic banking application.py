# OOP banking application
class atm:

    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
    Hi, How can i help you?
    1. Press 1 to create pin
    2. Press 2 to change pin
    3. Press 3 to check balance
    4. Press 4 to withdraw
    5. Anything else to exit""")
        
        if user_input == '1':
            self.create_pin()
            #create pin
        elif user_input == '2':
            self.change_pin()
            #change pin
        elif user_input == '3':
            self.check_balance()
            #check balance
        elif user_input == '4':
            self.withdraw()
            #withdraw
        else:
            exit()
    
    def create_pin(self):
        user_pin = input ('Enter your pin')
        self.pin = user_pin

        user_balance = int(input('Enter Balance'))
        self.balance = user_balance
        self.menu()

        print ('Pin created successfully')

    def change_pin(self):
        old_pin = input ('Enter old pin')

        if old_pin == self.pin:
            new_pin = input('Enter new pin')
            self.pin = new_pin
            print('PIN changed successfully')
            self.menu()
        else:
            print("Pin didn't match please try again")
            self.menu()

    def check_balance(self):
        user_pin = input('Enter your pin')
        if user_pin==self.pin:
            print('Your balance is', self.balance)
            self.menu()
        else: 
            print('Wrong pin try again')
            self.check_balance()

    def withdraw(self):
        user_pin = input('Enter your PIN - ')
        if user_pin == self.pin:
            withdraw_amount = int(input ('Enter the amount'))
            if withdraw_amount <= self.balance:
                self.balance = self.balance - withdraw_amount
                print('Withdrawal Successful and now your balance is', self.balance)
            else:
                print(" You don't have enough balance ")
            self.menu()
        else:
            print('Wrong PIN try again')
        self.menu()

        
obj = atm()

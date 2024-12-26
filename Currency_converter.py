import os

class CurrencyConverter:
    def __init__(self):
        self.exchange_rates = {
            'USD': 1.0,
            'EUR': 0.96,
            'INR': 85.47,
            'GBP': 0.80,
            'AUD': 1.60,
            'CAD': 1.44
            }
        
    def convert (self, selected_currency, target_currency, amount):
            if selected_currency not in self.exchange_rates and target_currency not in self.exchange_rates:
                raise ValueError('Currency not Found,\nPlease try again...')
            
            if amount < 0:
                raise ValueError('Amount cannot be negative:\nPlease try again...') 
            
            rate = self.exchange_rates[target_currency] / self.exchange_rates[selected_currency]
            return round(amount*rate, 2)
    
class ConversionHistory:
    def __init__(self):
        self.history = []

    def add_history (self, selected_currency, target_currency, amount,converted_amount):
        record = f"{amount} {selected_currency} = {converted_amount} {target_currency} "
        self.history.append(record)

    def save_history_to_file(self, filename = 'currency_converter_history.txt'):
        with open(filename, 'a') as file:
            for record in self.history:
                file.write(record + '\n')
        self.history = []

    def read_history_from_file(self, filename = 'currency_converter_history.txt'):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                return file.readlines()
        else:
            return[]   

class CLI:
    def __init__(self):
        self.converter = CurrencyConverter()
        self.history = ConversionHistory()

    def display_menu(self):
        while True:
         print('''
        Welcome to Currency Converter
        1. Convert Currency
        2. View History
        3. Exit
        We only convert USD, INR, EUR, AUD, CAD ,GBP
         ''')

         choice = input ('Choose an option: ')

         if choice == '1':
            self.handle_conversion()
         elif choice == '2':
             self.view_history()
         elif choice == '3':
             self.history.save_history_to_file()
             print ('Thank you for using the app. \nAdios!!')
             break
         else:
             print('Wrong Input...Try Again')
             return self.display_menu() 
         
    def handle_conversion(self):
        try:
         selected_currency = input('Enter the currency you want to convert:').upper()
         target_currency = input('Enter the currecny you want to convert to:').upper() 
         amount = float(input('Enter the amount you want to convert: '))

         converted_amount = self.converter.convert(selected_currency,target_currency,amount)

         print(f'{amount} {selected_currency} = {converted_amount} {target_currency}')

         self.history.add_history(selected_currency, target_currency, amount, converted_amount)
         
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def view_history(self):
        file_history = self.history.read_history_from_file()
        session_history = self.history.history

        print('Session History: ')
        if not file_history and not session_history:
            print('No history found')
        else:
            for record in file_history + session_history:
                print(record.strip())



if __name__ == '__main__':
    cli = CLI()
    cli.display_menu()
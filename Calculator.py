class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 +self.num2
    
    def diff(self):
        return self.num1 - self.num2
    
    def mul(self):
        return self.num1* self.num2
    
    def div(self):
        if self.num2 != 0:
            return self.num1/self.num2
        else:
            return 'Error'
    
num1 = float(input('Enter first number = '))
num2 = float(input('Enter second number = '))
operation = input('Choose Operation (+,-,*,/): ')


calc = Calculator(num1,num2)

if operation == "+":
    print(calc.add())
elif operation == "-":
    print(calc.diff())
elif operation == "*":
    print(calc.mul())
elif operation == "/":
    print(calc.div())
else:
    print('Invalid Operation')
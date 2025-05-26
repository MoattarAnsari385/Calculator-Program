operator = input("Choose an operator (+, -, *, /, %, **): ")
num1 = int(input("Enter a 1st number: "))
num2 = int(input("Enter a 2nd number: "))

if operator == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operator == '/':
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
elif operator == '**':
    result = num1 ** num2
    print(f"{num1} ** {num2} = {result}")
elif operator == '%':
    result = num1 % num2
    print(f"{num1} % {num2} = {result}")
else:
    print("Invalid operator. Please choose one of the following: +, -, *, /, %, **")

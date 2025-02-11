import inquirer

print('\tWelcome to my Calculator created by Qirat')


questions_for_calculation = [
        inquirer.Text('num1', message="Enter first number"),
        inquirer.Text('num2', message="Enter second number"),
         inquirer.List('operation', message="Choose an operation",  choices=['+', '-', '*', '/']),
    ]
# Here is inquirer prompt
answers = inquirer.prompt(questions_for_calculation)
num1 = float(answers['num1'])
num2 = float(answers['num2'])
operation = answers['operation']

if operation == '+':
        result = num1 + num2
        print(result)
elif operation == '-':
        result = num1 - num2
        print(result)
elif operation == '*':
        result = num1 * num2
        print(result)
elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            
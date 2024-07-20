# Step 1: Prompt User for Input
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
operation = input("Choose an operation (+, -, *, /): ")

# Step 2: Perform Calculation
if operation == '+':
    result = number1 + number2
elif operation == '-':
    result = number1 - number2
elif operation == '*':
    result = number1 * number2
elif operation == '/':
    if number2 != 0:
        result = number1 / number2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation selected."

# Step 3: Display Result
print("The result is:", result)

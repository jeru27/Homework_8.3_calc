
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

operation = input("Choose a math operation(+, -, /, *): ")

if operation == "+":
    print(x+y)
elif operation == "-":
    print(x-y)
elif operation == "/":
    print(x/y)
elif operation == "*":
    print(x*y)
else:
    print("You didn't provide a correct math operation.")

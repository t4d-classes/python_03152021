result = 0

command = input("Enter a command: ")

while command:

    if command == "add":
        num = float(input("Please enter an operand: "))
        result = result + num
    elif command == "subtract":
        num = float(input("Please enter an operand: "))
        result = result - num
    elif command == "multiply":
        num = float(input("Please enter an operand: "))
        result = result * num
    elif command == "divide":
        num = float(input("Please enter an operand: "))
        result = result / num
    elif command == "clear":
        result = 0

    print("Result: " + str(result))

    command = input("Enter a command: ")
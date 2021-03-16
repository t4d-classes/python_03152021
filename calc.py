result = 0
history = []
next_history_entry_id = 0

command = input("Enter a command: ")

while command:

    if command == "add":

        num = float(input("Please enter an operand: "))
        result = result + num

        next_history_entry_id = next_history_entry_id + 1
        history_entry = (next_history_entry_id, "add", num)
        history.append(history_entry)
        print("Result: " + str(result))

    elif command == "subtract":

        num = float(input("Please enter an operand: "))
        result = result - num

        next_history_entry_id = next_history_entry_id + 1
        history_entry = (next_history_entry_id, "subtract", num)
        history.append(history_entry)
        print("Result: " + str(result))

    elif command == "multiply":

        num = float(input("Please enter an operand: "))
        result = result * num

        next_history_entry_id = next_history_entry_id + 1
        history_entry = (next_history_entry_id, "multiply", num)
        history.append(history_entry)
        print("Result: " + str(result))

    elif command == "divide":

        num = float(input("Please enter an operand: "))
        result = result / num

        next_history_entry_id = next_history_entry_id + 1
        history_entry = (next_history_entry_id, "divide", num)
        history.append(history_entry)
        print("Result: " + str(result))

    elif command == "history":

        print(" Id | Op Name | Op Value ")
        print("-------------------------")

        for history_entry in history:
            print(str(history_entry[0]).rjust(3) +
                  " | " +
                  history_entry[1].ljust(7) +
                  " | " +
                  str(history_entry[2]).rjust(8))

    elif command == "remove":

        history_entry_id = int(input("Please enter a history entry id: "))

        for history_entry in history:
            if history_entry[0] == history_entry_id:
                history.remove(history_entry)
                break

    elif command == "clear":
        result = 0
        history = []

    command = input("Enter a command: ")

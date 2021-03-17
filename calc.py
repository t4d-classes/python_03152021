from functools import reduce

calc_ops = [
    {"id": 1, "label": "Add", "command": "add", "fn": lambda x, y: x + y},
    {"id": 2, "label": "Subtract", "command": "subtract", "fn": lambda x, y: x - y},
    {"id": 3, "label": "Multiply", "command": "multiply", "fn": lambda x, y: x * y},
    {"id": 4, "label": "Divide", "command": "divide", "fn": lambda x, y: x / y},
    {"id": 5, "label": "Exponent", "command": "exponent", "fn": lambda x, y: x**y},
]

history = []


def input_int(prompt):
    return int(input(prompt))


def input_float(prompt):
    return float(input(prompt))


def get_operand():
    return input_float("Please enter an operand: ")


def get_command():
    return input("Enter a command: ")


def get_history_entry_id():
    return input_int("Please enter a history entry id: ")


def create_history_entry(entry_id, op_name, op_value):
    return {"id": entry_id, "op_name": op_name, "op_value": op_value}


def append_history_entry(history_list, op_name, op_value):

    next_entry_id = max([h["id"] for h in history_list] or [0]) + 1

    new_history_entry = create_history_entry(
        next_entry_id, op_name, op_value)
    history_list.append(new_history_entry)


def calc_operation(result, entry):

    for calc_op in calc_ops:
        if entry["op_name"] == calc_op["command"]:
            calc_op_fn = calc_op["fn"]
            return calc_op_fn(result, entry["op_value"])

    return result


def calc_result(history_list):
    """ Iterates over the history list to calculate the result """
    return reduce(calc_operation, history_list, 0)
    # result = 0
    # for entry in history_list:
    #     result = calc_operation(result, entry)
    # return result


def display_operation_counts(history_list):

    calc_op_counts = []

    for calc_op in calc_ops:
        calc_op_count = len(
            [entry for entry in history_list if entry["op_name"] == calc_op["command"]])
        calc_op_counts.append((calc_op["label"], calc_op_count))

    print("Op Counts")
    print("---------")
    for calc_op_count in calc_op_counts:
        print(calc_op_count[0] + ": " + str(calc_op_count[1]))


def display_history(history_list):
    print(" Id | Op Name | Op Value ")
    print("-------------------------")

    for history_entry in history_list:
        print(str(history_entry["id"]).rjust(3) + " | " + history_entry["op_name"].ljust(7) +
              " | " +
              str(history_entry["op_value"]).rjust(8))


def remove_history_entry(history_list, entry_id):
    for entry in history_list:
        if entry["id"] == entry_id:
            history_list.remove(entry)
            break


op_commands = [calc_op["command"] for calc_op in calc_ops]

command = "clear"

while command:

    if command == "history":
        display_history(history)
        display_operation_counts(history)
    elif command == "remove":
        history_entry_id = get_history_entry_id()
        remove_history_entry(history, history_entry_id)
    elif command == "clear":
        history = []
    elif command in op_commands:
        num = get_operand()
        append_history_entry(history, command, num)
        print("Result: " + str(calc_result(history)))
    else:
        print("Invalid command. Would you like to play a nice game of chess?")

    command = get_command()

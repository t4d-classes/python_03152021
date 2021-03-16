from functools import reduce

calc_ops = [
    (1, "Add", "add", lambda x, y: x + y),
    (2, "Subtract", "subtract", lambda x, y: x - y),
    (3, "Multiply", "multiply", lambda x, y: x * y),
    (4, "Divide", "divide", lambda x, y: x / y),
    (5, "Exponent", "exponent", lambda x, y: x**y),
]

history = []
next_history_entry_id = 0


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
    return (entry_id, op_name, op_value)


def append_history_entry(history_list, entry_id, op_name, op_value):

    next_entry_id = entry_id + 1

    new_history_entry = create_history_entry(
        next_entry_id, op_name, op_value)
    history_list.append(new_history_entry)
    return next_entry_id


def calc_operation(result, entry):

    for calc_op in calc_ops:
        if entry[1] == calc_op[2]:
            calc_op_fn = calc_op[3]
            return calc_op_fn(result, entry[2])

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
            [entry for entry in history_list if entry[1] == calc_op[2]])
        calc_op_counts.append((calc_op[1], calc_op_count))

    print("Op Counts")
    print("---------")
    for calc_op_count in calc_op_counts:
        print(calc_op_count[0] + ": " + str(calc_op_count[1]))


def display_history(history_list):
    print(" Id | Op Name | Op Value ")
    print("-------------------------")

    for history_entry in history_list:
        print(str(history_entry[0]).rjust(3) + " | " + history_entry[1].ljust(7) +
              " | " +
              str(history_entry[2]).rjust(8))


def remove_history_entry(history_list, entry_id):
    for entry in history_list:
        if entry[0] == entry_id:
            history_list.remove(entry)
            break


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
    else:
        num = get_operand()
        next_history_entry_id = append_history_entry(
            history, next_history_entry_id, command, num)
        print("Result: " + str(calc_result(history)))

    command = get_command()

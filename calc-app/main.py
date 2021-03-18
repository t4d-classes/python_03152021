from input_console import get_history_entry_id, get_operand, get_command
from calc_ops import calc_ops, calc_op_commands
from history import History
import calc_view_console


def main():

    history = History(calc_ops)

    command = "clear"

    while command:

        if command == "history":
            calc_view_console.display_history(history)
            calc_view_console.display_operation_counts(history)
        elif command == "remove":
            history_entry_id = get_history_entry_id()
            history.remove(history_entry_id)
        elif command == "clear":
            history.clear()
        elif command in calc_op_commands:
            num = get_operand()
            # history.append(command, num)
            history += (command, num)
            print(f"Result: {history.result}")
        else:
            print("Invalid command. Please try again.")

        command = get_command()


if __name__ == '__main__':
    main()

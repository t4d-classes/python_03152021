from input_console import get_command
from calc_ops import calc_ops
from models.history import History
from commands import app_commands, command_unknown, log_command


def main():

    history = History(calc_ops)
    command = "clear"

    while command:
        log_command(command)
        command_fn = app_commands.get(command, command_unknown)
        command_fn(history)
        command = get_command()


if __name__ == '__main__':
    main()

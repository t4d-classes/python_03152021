from color_list import ColorList
from list_console_view import ListConsoleView


def main():

    colors = ColorList()

    command = input("Please enter a command > ")

    while command:

        if command == "append":
            color_name = input("Color Name > ")
            color_hexcode = input("Color Hexcode > ")
            colors.append(color_name, color_hexcode)
        elif command == "remove":
            color_id = int(input("Enter a Color Id to Remove > "))
            colors.remove(color_id)
        elif command == "clear":
            colors.clear()
        elif command == "count":
            list_console_view = ListConsoleView(colors)
            list_console_view.display_count()
        elif command == "list":
            list_console_view = ListConsoleView(colors)
            list_console_view.display_table()
        command = input("Please enter a command > ")


if __name__ == '__main__':
    main()

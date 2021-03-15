colors = []

last_color_id = 0

command = input("Please enter a command > ")

while command:

    if command == "append":
        color_name = input("Color Name > ")
        color_hexcode = input("Color Hexcode > ")
        last_color_id = last_color_id + 1
        color = (last_color_id, color_name, color_hexcode)
        colors.append(color)
    elif command == "remove":
        color_id = int(input("Enter a Color Id to Remove > "))

        for color in colors:
            if color_id == color[0]:
                colors.remove(color)
                break

    elif command == "clear":

        colors.clear()

    elif command == "count":

        print("Number of Colors: " + str(len(colors)))

    elif command == "list":
        print("Id  Name            Hexcode")
        print("---------------------------")
        for color in colors:
            print(str(color[0]).rjust(2) + ' ' + color[1].ljust(15) + ' ' + color[2])

    command = input("Please enter a command > ")

colors = []

command = input("Please enter a command > ")

while command:

    if command == "append":
        color_name = input("Color Name > ")
        color_hexcode = input("Color Hexcode > ")
        next_color_id = max([c["id"] for c in colors] or [0]) + 1

        color = {
            "id": next_color_id,
            "name": color_name,
            "hexcode": color_hexcode,
        }

        colors.append(color)
    elif command == "remove":
        color_id = int(input("Enter a Color Id to Remove > "))

        for color in colors:
            if color_id == color["id"]:
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
            print(str(color["id"]).rjust(2) + ' ' +
                  color["name"].ljust(15) + ' ' + color["hexcode"])

    command = input("Please enter a command > ")

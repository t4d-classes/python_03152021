

class ColorListConsoleView:

    def __init__(self, color_list):
        self.color_list = color_list

    def display_count(self):
        print("Number of Colors: " + str(len(self.color_list)))

    def display_table(self):
        print("Id  Name            Hexcode")
        print("---------------------------")
        for color in self.color_list:
            print(str(color.id).rjust(2) + ' ' +
                  color.name.ljust(15) + ' ' + color.hexcode)

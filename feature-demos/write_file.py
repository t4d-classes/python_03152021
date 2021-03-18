
colors = ["red", "green", "blue"]

with open("newcolors.txt", "a") as new_colors_file:
    for color in colors:
        new_colors_file.write(f"{color}\n")

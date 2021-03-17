from color import Color


class ColorList:

    def __init__(self):
        self.colors = []

    def append(self, color_name, color_hexcode):
        next_color_id = max([c.id for c in self.colors] or [0]) + 1
        new_color = Color(next_color_id, color_name, color_hexcode)
        self.colors.append(new_color)

    def remove(self, color_id):
        for color in self.colors:
            if color_id == color.id:
                self.colors.remove(color)
                break

    def clear(self):
        self.colors.clear()

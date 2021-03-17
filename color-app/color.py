

class Color:

    def __init__(self, color_id, color_name, color_hexcode):
        self.id = color_id
        self.name = color_name
        self.hexcode = color_hexcode


    def label(self):
        # "red (ff0000)"
        return f"{self.name} ({self.hexcode})"

import csv
from color import Color


class ColorList:

    def __init__(self):
        self._colors = []  # composition

    def append(self, color_name, color_hexcode):
        next_color_id = max([c.id for c in self._colors] or [0]) + 1
        new_color = Color(next_color_id, color_name, color_hexcode)
        self._colors.append(new_color)

    def remove(self, color_id):
        for color in self._colors:
            if color_id == color.id:
                self._colors.remove(color)
                break

    def clear(self):
        self._colors.clear()

    def headers(self):
        return ["Id", "Name", "Hexcode"]

    def __len__(self):
        return len(self._colors)

    def __iter__(self):
        return iter(self._colors)

    def __next__(self):
        return next(self._colors)

    def save(self, csv_file_name):

        with open(csv_file_name, "w") as csv_file:
            writer = csv.DictWriter(
                csv_file, fieldnames=[
                    "id", "name", "hexcode"])
            writer.writeheader()
            for color in self._colors:
                writer.writerow(color.__dict__)

    def load(self, csv_file_name):

        with open(csv_file_name, "r") as csv_file:
            color_rows = csv.DictReader(csv_file)

            self._colors = [Color(int(c["id"]), c["name"], c["hexcode"])
                            for c in color_rows]

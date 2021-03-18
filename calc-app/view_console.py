

class ViewConsole:

    @staticmethod
    def display_table(columns, rows):

        headers = [c[0].ljust(c[2]) for c in columns]

        header_output = " | ".join(headers)

        print(header_output)
        print("-" * len(header_output))

        for row in rows:
            row_data = [str(row[c[1]]).ljust(c[2]) for c in columns]
            print(" | ".join(row_data))

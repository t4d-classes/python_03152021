import re

content = "as busy as a bee"

r = re.compile(r'as')

# match from the start of the string
# print(r.match(content))

# find the first match
# print(r.search(content))

# find all matches, but return a list of the just the strings which matched
# print(r.findall(content))

# find all matches, and return match objects
# print(list(r.finditer(content)))

# content = "red|green;blue:orange"
# r = re.compile(r"\||:|;")
# print(r.split(content))
# print(r.sub(",", content))

# content = "red|green;blue:orange"
# r = re.compile(r"[|:;]")
# print(r.split(content))
# print(r.sub(",", content))

# content = """apple
# banana
# apple
# banana
# banana
# Apple
# """

# # r = re.compile(r"^a[a-z]*")
# # r = re.compile(r"^a[a-z]*", re.MULTILINE | re.IGNORECASE)
# # r = re.compile(r"[a-z]*a$", re.MULTILINE | re.IGNORECASE)
# r = re.compile(r"[a-z]*a$")

# print(list(r.finditer(content)))

# content = "<b>content 1</b><span>test</span><b>content 2</b><div>fun</div>"

# # r = re.compile(r"<span>(.*)</span>")
# # r = re.compile(r"<b>(.*?)</b>")
# r = re.compile(r"<.*?>(.*?)</.*?>")

# # print(list(r.finditer(content)))

# for match in r.finditer(content):
#     print(match.groups()[0])

r = re.compile(r"Add: ([0-9]*)")

with open("./report.txt", "r") as report_file:
    report_content = report_file.read()
    add_count_match = r.search(report_content)
    print(add_count_match.groups()[0])

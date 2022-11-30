"""
How to create a table from txt file
by Over-k
"""

from faker import Faker #For generate cells 'information' u can use your csv file...
fake = Faker()

columns = ["Name", "Country", "Phone Number","Email", "Password"] # columns header (Change also the 'cells' variable)
rows    = 100 # Number of rows
l = 20  # Number of letters in cell #...max(sorted(your_list_words, key=len)[-1],30)



# Write lines to the file
def data(stat):
    with open('data.txt', 'a') as f:
        f.write(stat)
        f.close()

# Keep the same number of letters in all cells
def truncate(word):
    a = len(word)
    b = l - a
    return f"{word[:l-2]}.." if a > l else f"{word}{(' ')*b}"

# Type the table column header
header = ""
border = ""
for r in columns:
    header += f"|{truncate(r)}"
    border += f"+{('-')*l}"
data(f"{border}+\n")
data(f"{header}|\n")
data(f"{border}+\n")
# Row cell generation
for _ in range(rows):
    cells = [fake.name(), fake.country(), fake.phone_number(),fake.email(), fake.password()]
    row   = ""
    for cell in cells:
        row += f"|{truncate(cell)}"
    data(f"{row}|\n")

# Close the table
data(f"{border}+\n")

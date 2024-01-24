# Using generators to avoid loading the whole dataset at once to save memory
file_name = "techcrunch.csv"

# lines is a generator object returning one line at a time
lines = (line for line in open(file_name))

# Another generator that is splitting up the lines and getting rid of whitespace
list_line = (s.rstrip().split(",") for s in lines)

# Save the column names in cols
cols = next(list_line)

# Use a generator to zip col, data into dictionaries
company_dicts = (dict(zip(cols, data)) for data in list_line)

# Answer the question: how much was raised for series A
funding = (
    int(company_dict["raisedAmt"])
    for company_dict in company_dicts
    if company_dict["round"] == "a"
)

total_series_a = sum(funding)

print(f"Total series A fundraising: ${total_series_a}")





"""
import csv

with open('techcrunch.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
"""
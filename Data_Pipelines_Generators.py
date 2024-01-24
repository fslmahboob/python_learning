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
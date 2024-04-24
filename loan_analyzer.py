import csv
from pathlib import Path

# PART 1: Analyze Loan Data

# List of loan amounts, reflecting the initial investment in various loans.
loan_costs = [500, 600, 200, 1000, 450] # creates variable `loan_costs`

# Calculates the total number of loans in the portfolio.
count_loans = len(loan_costs) # creates variable `count_loans`

# Sums the total value of all loans.
total_lending = sum(loan_costs) # creates variable `total_lending`


# Calculates the average loan amount across all loans in the portfolio.
avg_loan_size = total_lending / count_loans # calculates and creates variable `avg_loan_size`

# Defines function `underline` | uses `join` method | joins each character in the string with an underline character (\u0332)
def underline(text):
    print("\u0332".join(text))

# Adds a blank line for visual separation.
print("\n")

# Prints the provided text with an underline effect.
underline("\tMODULE 1 CHALLENGE\n") 

print("Part 1: Automate the Calculations\n")   
print(f"\tThere are {count_loans} loans in this portfolio.")

# Formats the value of variable with commas and two decimal places for readability.
print(f"\tTotal amount lent out by this portfolio is $ {total_lending:,.2f}")
print(f"\tThe average loan size in this portfolio is $ {avg_loan_size:,.2f}\n")

 # Adds five blank lines for visual separation
for _ in range(5): 
    print()



# PART 2: Analyze Loan Data

# Dictionary representing a single loan's details.
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Accessing elements from the 'loan' dictionary using the .get() method:
# This method returns the value for the specified key if the key is in the dictionary.

# Retrieve 'loan_price' from 'loan' dictionary. Returns None if key is not found.
loan_sample = loan.get("loan_price")

# Retrieve 'future_value' from 'loan', key for expected value at loan maturity.
future_value = loan.get("future_value")

# Retrieve 'remaining_months' from 'loan', key for months until loan maturity.
remaining_months = loan.get("remaining_months")

# Sets annual discount rate.
discount_rate = 0.20 

# Calculates the present value of the loan based on its future value, discount rate, and remaining months.
present_value = future_value / (1 + discount_rate / 12) ** remaining_months

# Defines a function to calculate the fair value of a loan given its future value, annual discount rate, and time remaining in months.
def fair_value_calculator(future_value, annual_rate, months_remaining):
    return future_value / (1 + annual_rate / 12) ** months_remaining

# Starts output of loan data analysis.
print("Part 2: Analyze Loan Data\n")
print("\tGIVEN LOAN DATA:\n")

# Displays the future value of the loan
print(f"\t1. The 'Future Value' of the loan is $ {future_value:,.2f}")

# Displays the number of months until the loan matures.
print(f"\t2. There are {remaining_months} months left until this loan matures.")

# Display the annual interest rate applied to the loan.
print(f"\t3. The 'Annual Interest Rate' of the $ {loan_sample:,.2f} loan is {100 * discount_rate}%\n")

# Shows the calculated present value, referred to as the 'Fair Value' of the loan.
print(f"\tThe 'Present Value' of the loan is $ {present_value:,.2f} which is a.k.a its 'Fair Value'\n")

# Shows the calculated present value, referred to as the 'Fair Value' of the loan.
print(f"\tTherefore the 'Fair Value' of this loan is $ {present_value:,.2f}\n")

loan_sample = loan.get("loan_price")  # This retrieves the loan's purchase price.


# # Concludes with the decision on the loan's worthiness based on its fair value compared to its future value.
# if present_value >= loan_sample:
#         print(f"\tSince the 'Fair Value' is $ {future_value - present_value:,.2f} less than its 'Future Value' of $ {future_value:,.2f} at maturity,\n")
#         print(f"\tThe loan is worth at least the cost to buy for $ {present_value:,.2f}, which is it's 'Present Value' today.\n")

# # Indicates that the loan is overpriced compared to its future value.
# else:
#         print(f"\tSince the 'Fair Value' of the loan today is more than its 'Future Value' of $ {future_value:,.2f} at maturity.\n")
#         print("\tThe loan is too expensive and not worth the price.")

if present_value >= loan_sample:
    print(f"\tSince the 'Present Value' of $ {present_value:,.2f} is equal to or greater than its purchase price of $ {loan_sample:,.2f},\n")
    print(f"\tThe loan is worth buying at the price of $ {loan_sample:,.2f}.\n")
else:
    print(f"\tSince the 'Present Value' of $ {present_value:,.2f} is less than its purchase price of $ {loan_sample:,.2f},\n")
    print("\tThe loan is too expensive and not worth buying at this price.")

# Part 3: Perform financial calculations using functions.

# Defines a dictionary with new loan parameters.
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Retrieves data from the 'new_loan' dictionary using the .get() method, ensuring safe access.
new_loan_sample = new_loan.get("loan_price")
new_loan_remaining_months = new_loan.get("remaining_months")
new_loan_future_value = new_loan.get("future_value")
new_loan_costs = new_loan.get("loan_price")

# Calculates the present value of the new loan using a previously defined function 'fair_value_calculator'.
new_present_value = fair_value_calculator(new_loan_future_value, discount_rate, new_loan_remaining_months)

# Prints out the new loan data analysis results.
print("Part 3: Perform Financial Calculations\n")
print("\tGIVEN LOAN DATA:\n")
print(f"\t1. The 'Future Value' of the loan is $ {new_loan_future_value:,.2f}")
print(f"\t2. There are {new_loan_remaining_months} months left until this new loan matures.")
print(f"\t3. The 'Annual Interest Rate' of the new loan for $ {new_loan_sample:,.2f} is {100 * discount_rate}%\n")
underline(f"\tSOLUTION:\n")
print(f"\tThe present value of the new loan is: ${new_present_value:,.2f}\n")



# Part 4: Conditionally filter lists of loans

# Defines a list of dictionaries, each representing a loan with specific attributes.
loans = [
    {"loan_price": 700, "remaining_months": 9, "repayment_interval": "monthly", "future_value": 1000},
    {"loan_price": 500, "remaining_months": 13, "repayment_interval": "bullet", "future_value": 1000},
    {"loan_price": 200, "remaining_months": 16, "repayment_interval": "bullet", "future_value": 1000},
    {"loan_price": 900, "remaining_months": 16, "repayment_interval": "bullet", "future_value": 1000},
]

# Initializes an empty list to store loans priced at $500 or less.
inexpensive_loans = [] 

loan_index = [] #  <-- empty list

for chk_price in loans:     
    if chk_price['loan_price'] <= 500:
        inexpensive_loans.append(chk_price)
        loan_index.append(loans.index(chk_price)) # Stores index of inexpensive loans.


# Output the process of filtering loans based on price.
print("Part 4: Conditionally filter lists of loans\n")
count_items_in_loans = len(loans)
count_loan_index = len(loan_index)        


print(f"\tFirst we are given a loan inventory to evaluate to determine which loans are 'inexpensive'.")
print(f"\t'Inexpensive' is defined as having a 'loan price' less than or equal to $500")
print(f"\tThe inventory is in the form of a list of {count_items_in_loans} loans.\n")
print("\tTo solve, we iterate over the list to find the 'inexpensive loans'.\n") 
print(f"\tThe {count_loan_index} 'inexpensive loans' in the portfolio are:\n")

for price_only in inexpensive_loans:
    print("\t$ {}".format(price_only["loan_price"])) # Displays prices of inexpensive loans.


# # Modify and print each inexpensive loan's details in a more readable format
# print("Detailed Information of Inexpensive Loans:")
# for loan in inexpensive_loans:
#     repayment_term = "End-term Lump Sum" if loan['repayment_interval'] == 'bullet' else loan['repayment_interval']
#     print(f"Loan Price: ${loan['loan_price']}, Remaining Months: {loan['remaining_months']}, Repayment Interval: {repayment_term}, Future Value: ${loan['future_value']}")

# Part 5: Save the results.

print("\n")
print("Part 5: Save the results\n")

# # Notifies the user of the action to take place.
# print("The final step in this challenge is to save our results by writing a .csv file named 'inexpensive_loans.csv'\n")

# # Confirms which part of the loan data will be saved.
# print(f"From the original {count_items_in_loans} loans in the given portfolio, we are asked to save the 'inexpensive loans' only.\n")

# # Provides feedback that saving process is starting.
# underline(f"... SAVING THE '{count_loan_index} inexpensive loans' shown below using csv module in Python.\n")

# # Defines the CSV file path and set the header for the CSV file.
# header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]
# output_path = Path("inexpensive_loans.csv")

# # Opens the file in write mode and write the header and rows.
# csvpath = Path("inexpensive_loans.csv")
# with open(csvpath, 'w', newline='') as inexpensive_csv:
#     csv_writer = csv.writer(inexpensive_csv)
#     csv_writer.writerow(header)             # this line creates the 'header' in the csv file
#     for row in inexpensive_loans:
#         csv_writer.writerow(row.values())   # this line saves the 'inexpensive loans in the .csv
#         print(row)                          # this line prints the 'inexpensive loans' into the terminal terminal window

# Notifies the user of the action to take place.
print("The final step in this challenge is to save our results by writing a .csv file named 'inexpensive_loans.csv'\n")

# Confirms which part of the loan data will be saved.
print(f"From the original {count_items_in_loans} loans in the given portfolio, we are asked to save the 'inexpensive loans' only.\n")

# Provides feedback that saving process is starting.
underline(f"... SAVING THE '{count_loan_index} inexpensive loans' shown below using csv module in Python.\n")

# Defines the CSV file path and sets the header for the CSV file.
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]
output_path = Path("inexpensive_loans.csv")

# Opens the file in write mode and writes the header and rows.
csvpath = Path("inexpensive_loans.csv")
with open(csvpath, 'w', newline='') as inexpensive_csv:
    csv_writer = csv.writer(inexpensive_csv)
    csv_writer.writerow(header)  # This line creates the 'header' in the csv file
    for loan in inexpensive_loans:
        csv_writer.writerow([loan['loan_price'], loan['remaining_months'], loan['repayment_interval'], loan['future_value']])
        
# Modify and print each inexpensive loan's details in a more readable format
print("Detailed Information of Inexpensive Loans being saved in CSV file:")
for loan in inexpensive_loans:
    repayment_term = "End-term Lump Sum" if loan['repayment_interval'] == 'bullet' else loan['repayment_interval']
    print(f"Loan Price: ${loan['loan_price']}, Remaining Months: {loan['remaining_months']}, Repayment Interval: {repayment_term}, Future Value: ${loan['future_value']}")

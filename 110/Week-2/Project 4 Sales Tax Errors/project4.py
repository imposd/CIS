# Kyle Bennett
# Sept. 5th, 2024
# Project 4

# Assign the tax rate
tax_rate = 0.06

# Gather sale amount from user
sale = float(input('Enter the purchase amount: $'))
# Multiply sale amount that the user provided and tax rate together to make sales tax
sales_tax = sale * tax_rate
# Add input from user and the sales tax to get a total value
total = sale + sales_tax

print('Purchase amount: $', sale)
print('Sales tax amount: $', sales_tax)
print('Total due: $', total)

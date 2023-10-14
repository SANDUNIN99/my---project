def calculate_income_tax(income):
    if income <= 100000:
        tax = 0
    elif income <= 500000:
        tax = 0.20 * (income - 100000)
    else:
        tax = 0.30 * (income - 500000)
    return tax

# Get user input for income
income = float(input("Enter your income: $"))

# Calculate the income tax
tax = calculate_income_tax(income)

# Display the result
print(f"Your income tax is: ${tax:.2f}")
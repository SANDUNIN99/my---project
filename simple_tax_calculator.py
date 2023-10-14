def calculate_income_tax(income):
    if income <= 75000:
        tax = 0
    elif income <= 200000:
        tax = 0.20 * (income - 75000)
    else:
        tax = 0.30 * (income - 75000)
    return tax


# Get user input for income
income = float(input("Please enter your income: $"))

# Calculate the income tax
tax = calculate_income_tax(income)

# Display the result
print(f"Your income tax is: ${tax:.2f}")

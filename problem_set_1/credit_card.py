try:
    outstanding_balance = float(input("Enter the outstanding balance on your credit card: "))
    annual_rate = float("0" + input("Enter the annual credit card interest rate as adecimal: "))
    minimum_rate = float("0" + input("Enter the minimum monthly payment rate as a decimal: "))
except:
    print("Invalid input.")
    outstanding_balance = 4800
    annual_rate = 0.2
    minimum_rate = 0.02

def month_balance(outstanding_balance, annual_rate, minimum_rate):
    minimum_payment = minimum_rate * outstanding_balance
    interest_paid = (annual_rate/12) * outstanding_balance
    principal_paid = minimum_payment - interest_paid
    print("Minimum monthly payment: $%.2f\nPrinciple paid: $%.2f\nRemaining balance: $%.2f" % (minimum_payment, principal_paid, (outstanding_balance - principal_paid)))
    return outstanding_balance - principal_paid, interest_paid + principal_paid

total_paid = 0
for month in range(12):
    print("Month:", month+1)
    outstanding_balance, paid = month_balance(outstanding_balance, annual_rate, minimum_rate)
    total_paid += paid

print("RESULT")
print("Total amount paid: %.2f" % total_paid)
print("Remaining balance: %.2f" %  outstanding_balance)

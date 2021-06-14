try:
    outstanding_balance = float(input("Enter the outstanding balance on your credit card: "))
    annual_rate = float("0" + input("Enter the annual credit card interest rate as a decimal: "))
except:
    print("Invalid input.")
    outstanding_balance = 1200
    annual_rate = 0.18

monthly_rate = annual_rate / 12
payment = outstanding_balance / 12
if payment % 10 != 0:
    payment = payment - (payment % 10)

def is_paid (payment, outstanding_balance, annual_rate):
    for month in range(12):
        outstanding_balance = outstanding_balance * (1 + monthly_rate) - payment
    return outstanding_balance

paid = False
while paid == False:
    if is_paid(payment, outstanding_balance, annual_rate) <= 0:
        paid = True
    else:
        payment += 10

no_of_months = int()
for month in range(12):
    outstanding_balance = outstanding_balance * (1 + monthly_rate) - payment
    if outstanding_balance < 0:
        no_of_months = month + 1
        break

print("RESULT")
print("Monthly paymnt to pay off debt in 1 year:", payment)
print("Number of months needed:", no_of_months)
print("Balance: %.2f" % outstanding_balance)

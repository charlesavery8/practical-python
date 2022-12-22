# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0

extra = 1000
st_extra = 60
end_extra = 108


while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    if st_extra < months <= end_extra :
        principal -= extra
        total_paid += extra
    months += 1
    if principal < 0:
        total_paid -= abs(principal)
        principal += abs(principal)    
    print(months, total_paid, principal)

print("Total Paid:", total_paid, "\n", "Months:", months)


# pcost.py
#
# Exercise 1.27
Total_cost = 0
with open('C:/Users/avery/OneDrive/Documents/GitHub/practical-python$$$/Work/Data/portfolio.csv', 'rt') as f:
    skip = next(f)
    for line in f:
        row =line.split(",")
        shares = float(row[1])
        price = float(row[2])
        Total_cost = price *shares
print('Total Cost:', Total_cost)

expense_list = {'jan':2340, 'feb':2500, 'mar':2100, 'apr':3100, 'may':2980}
expense = input("Enter expense: ")

month = None
for key,val in expense_list.items():
    if val == int(expense):
        month = key

if month != None:
    print(f"The expense is made in the month of {month}")
else:
    print("No such expense has been made in previous months")
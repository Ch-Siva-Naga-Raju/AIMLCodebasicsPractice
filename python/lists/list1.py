expenses = [2200, 2350, 2600, 2130, 2190]

print(expenses[1] - expenses[0])

print(f"The total First Quarter expense is: ${str(expenses[0] + expenses[1] + expenses[2])}" )

flag = False
for i in range(len(expenses)):
    if expenses[i] == 2000:
        flag = True
        break
print(flag)


expenses.append(1980)

expenses[3] = expenses[3] - 200

for i in range(len(expenses)):
    print(expenses[i])


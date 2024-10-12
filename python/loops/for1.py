result = ["tails","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
headcount = 0
for i in range(len(result)):
    if result[i] == 'heads':
        headcount = headcount + 1

print(f"The result has {str(headcount)} heads and {str(len(result) - headcount)} tails")
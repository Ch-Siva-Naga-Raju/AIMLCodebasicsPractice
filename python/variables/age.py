birthYear = 1991
currentYear = 2024

def calculateAge(bYear,cYear):
    if(bYear < cYear):
        print('You are ' + str(cYear-bYear) + ' years old.')
    else:
        print('So... are you from the future?')

if __name__ == "__main__":
    calculateAge(birthYear,currentYear)
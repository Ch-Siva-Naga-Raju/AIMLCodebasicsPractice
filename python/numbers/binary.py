def getBinaryNotation():
    num = int(input("Enter an positive integer number: "))
    result = ""
    if(num < 0): 
        print("Invalid input (basically we're not handling them in this program)")
    while num >= 1:
        result = str(num%2) + result
        num = int(num/2)
    print("The binary representation of the given number is: "+ result)

if __name__ == "__main__":
    getBinaryNotation()
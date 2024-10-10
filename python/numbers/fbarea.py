def getFieldArea():
    length = input("Enter Foodball Field length in meters: ")
    width = input("Enter Foodball Field width in meters: ")
    print("Area of the Foodball Field is: " + str(round(float(length) * float(width), 2)))

if __name__ == "__main__":
    getFieldArea()
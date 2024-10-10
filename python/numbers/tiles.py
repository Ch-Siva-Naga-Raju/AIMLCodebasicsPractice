import math
def calculateCost():
    side = input("Enter side length of the square room in foot: ")
    roomArea = float(side)**2
    tileCostPerSqFt = input("Enter the tile cost per square foot: ")
    tileCount = math.ceil(roomArea)
    print("The cost of the tiles is: "+ str(round(float(tileCostPerSqFt) * tileCount),2))

if __name__ == "__main__":
    calculateCost()
def calculateBalance():
    quantity = input("Enter the number of chips packets purchased: ")
    itemPrice = input("Enter the price of each chips packet: ")
    payment = input("Enter the amout you paid to the shopkeeper: ")
    balance = float(payment) - int(quantity) * float(itemPrice)
    if(balance < 0):
        print("You have to give the shopkeeper "+ str(round(-balance,2)))
    else:
        print("The shopkeeper should give you "+ str(round(balance,2)))

if __name__ == "__main__":
    calculateBalance()
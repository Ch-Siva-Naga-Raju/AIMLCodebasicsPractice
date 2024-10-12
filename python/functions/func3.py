def print_pattern():
    val = input("Enter an integer: ")
    for i in range(int(val)+1):
        s = ""
        for j in range(i):
            s+= " *"
        print(s)

print_pattern()
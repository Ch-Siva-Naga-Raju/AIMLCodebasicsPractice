india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
citylist = india + pakistan + bangladesh
print("List of Cities: ")
print(citylist)
chosencity = input("Enter a city of your choice from the above list: ")
iscityfound = False
for i in range(max(len(india), len(pakistan), len(bangladesh))):
    if i < len(india) and india[i] == chosencity:
        print("The city you chose is in India")
        iscityfound = True
    elif i < len(pakistan) and pakistan[i] == chosencity:
        print("The city you chose is in Pakistan")
        iscityfound = True
    elif i < len(bangladesh) and bangladesh[i] == chosencity:
        print("The city you chose is in Bangladesh")
        iscityfound = True

if not iscityfound:
    print("Please enter a city from the list provided.")
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
citylist = india + pakistan + bangladesh
print("List of Cities: ")
print(citylist)
chosencity1 = input("Enter a city from the above list: ")
chosencity2 = input("Enter another city from the above list: ")
iscity1found = False
iscity2found = False
country1 = ""
country2 = ""
for i in range(max(len(india), len(pakistan), len(bangladesh))):
    if i < len(india) and (india[i] == chosencity1 or india[i] == chosencity2):
        if india[i] == chosencity1:
            country1 = "India"
            iscity1found = True
        if india[i] == chosencity2:
            country2 = "India"
            iscity2found = True
    elif i < len(pakistan) and (pakistan[i] == chosencity1 or pakistan[i] == chosencity2):
        if pakistan[i] == chosencity1:
            country1 = "pakistan"
            iscity1found = True
        if pakistan[i] == chosencity2:
            country2 = "pakistan"
            iscity2found = True
    elif i < len(bangladesh) and (bangladesh[i] == chosencity1 or bangladesh[i] == chosencity2):
        if bangladesh[i] == chosencity1:
            country1 = "bangladesh"
            iscity1found = True
        if bangladesh[i] == chosencity2:
            country2 = "bangladesh"
            iscity2found = True

if not iscity1found or not iscity2found:
    print("Please enter a city from the list provided.")

if country1 == country2:
    print(f"Both the cities are in {country1}")
else:
    print("Both the cities are in different countries")
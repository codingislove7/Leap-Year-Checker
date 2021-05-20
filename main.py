# Say Hello
print("Welcome to leap year checker:)")
# Get the Year
year = int(input("enter the year:\n"))
# some logic and magic happens
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a Leap Year.")
        else:
            print(f"{year} is Not a Leap Year.")
    else:
        print(f"{year} is a Leap Year.")
else:
    print(f"{year} is Not a Leap Year.")
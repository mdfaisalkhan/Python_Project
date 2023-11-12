
year = input("Enter the Current year= ")
school = input("Enter the school Establish year= ")
cls = input("Enter the class in digit= ")
roll = input("Enter the student roll no= ")

# Check if the year input is valid
if len(year) != 4 or not year.isdigit():
    print("Year should be a 4-digit number.")
else:
    y1 = year[2:]
    
if len(school) != 4 or not school.isdigit():
    print("school year should be a 4-digit number.")
else:
    s1 = school[2:]

    # Check if the roll input is valid
    if not roll.isdigit() or len(roll) != 2:
        print("Enter a 2-digit roll number like: 01, 02, etc.")
    else:
        # Check if the class is within the valid range
        if cls.isdigit() and 0 < int(cls) < 13:
            print(y1 + s1 + cls + roll)
        else:
            print("Class should be a number greater than 0 and less than 13.")

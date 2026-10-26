marks = int(input("Enter Marks: "))

if marks >= 90:
    print("Grade A")
elif marks <= 89 and marks >= 75:
    print("Grade B")
elif marks <= 74 and marks >= 40:
    print("Grade C")
else:
    print("Fail")
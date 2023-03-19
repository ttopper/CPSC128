# validating_input.py
print("Instructions to user...")
grade = float(input("Enter a numerical grade between 0 and 100: "))

while grade>100 or grade<0:
    print("Error: The grade must be between 0 and 100.")
    grade = float(input("Enter a numerical grade between 0 and 100: "))

if grade>=95:
    print("A+")
elif grade>= 86:
    print("A")

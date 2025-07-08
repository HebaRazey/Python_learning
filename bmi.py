#The BMI is a convenient rule of thumb;
# used to broadly categorize a person as based on tissue mass (muscle, fat, and bone) and height
mass= int(input("Enter mass in Kg: "))
height= float(input("Enter height in meters: "))
bmi= mass/(height**2)
print(f"Your BMI= {bmi}")
print("")
print("Standard BMI values for comparison=")
print("  Less than 18.5: underweight")
print("  Between 18.5 and 24.9: Normal")
print("  Between 25 and 29.9: Overweight")
print("  Greater than 30: Obese")
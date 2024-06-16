height = float(input("Enter your height in centimeters: "))
weight = float(input("Enter your weight in Kilograms: "))
height = height/100
BMI = weight/(height*height)
print("Your BMI is: ", BMI)
if BMI <= 16:
    print("You are severely underweight")
elif BMI <= 18.5:
    print("You are underweight")
elif BMI <= 25.0:
    print("You are Healthy")
elif BMI >= 30.0:
    print("You are overweight")
else:
    print("You are obese")


print("This program calculates the BMI of a person")

weight=float(input("Please type your weight in kilograms: "))
height=float(input("Please type your height in meters: "))

bmi=weight/(height*height)

print("Your BMI is: ",round(bmi,2))

if(bmi<=18.5):
     print("Underweight")
elif(bmi>18.5 and bmi<=24.9):
    print("Normal weight")
elif(bmi>24.9 and bmi<=29.9):
    print("Overweight")
else:
    print("Obesity")


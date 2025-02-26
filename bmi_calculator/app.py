# formula for bmi 
# bmi = weight(kg) / height(m)**2
height = float(input("Enter your height in meter: "))
weight = float(input("Enter your weight in kg: "))   
bmi = weight / (height ** 2)
print(f'Your BMI is:{round(bmi,2)}')

if bmi < 18.5:
    print("You are underweight.")
elif bmi >= 18.5 and bmi < 25:
    print("You are normal weight.")
elif bmi >= 25 and bmi < 30:
    print("You are overweight.")
elif bmi >= 30:
    print("You are obese.")

print("BMI Calculator ")

gender=input("your Gender= ")
age=input("What is your agr= ")
weight=float(input("What is your weight in (kg)= "))
height=float(input("What is your height in (meter)= "))

#Calculate & Print
BMI=round((weight)/(pow(height,2)),2)


if BMI < 18.5:
    print(f'Your BMI is {BMI}, You are Under Weight')

elif BMI in range(18.5,25):
    print(f'Your BMI is {BMI}, You are Normal Weight')

elif BMI in range(25,30):
    print(f'Your BMI is {BMI}, You are Over Weight')

elif BMI >= 30 :
    print(f'Your BMI is {BMI}, You are Obesity')     
    
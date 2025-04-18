#Write the code that calculates the person's weight index and returns the result as underweight, overweight or overweight according to the index value. (You can look on the internet for the weight index calculation) To do this, ask the user for their weight and height measurements. weight index If it is below 25, it is weak, Between 25-30 is normal, If you are over 30-40, you are overweight. If you are over 40, you are overweight
weight = float(input("Enter your weight in kilograms: ")) #float(input(...)) function is used to allow decimal inputs for weight and height
height = float(input("Enter your height in meters; "))

bmi = weight /(height ** 2)

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi <25:
    category = "Normal weight"
elif 25 <= bmi <30:
    category = "Overweight"
else:
    category = "Obesity"

print(f"Your BMI is: {bmi:.2f}") #:.2f formatting in the print statement rounds the BMI to two decimal places for readability.
print(f"You are classified as: {category}")

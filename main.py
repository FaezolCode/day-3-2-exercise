# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round (weight / height **2)

if bmi == 18.5:
  print ("you're underweight")

elif bmi <=25:
  print("you're normal weight")
elif bmi <=30:
  print("you're slightly overweight")
elif bmi <=35:
  print("you're obese")
else:
  print("you're clinically obese")






#This program converts body weight from from into kilogram according to the user input.

#Defines the input
body_weight = int(input("\n weight in pounds:\n"))

#Calculation
body_weight_calculator = body_weight / 2.204

#Rounded the float to 3 decimals.
rounded_weight = round(body_weight_calculator, 3)

#print the result on the screen.
print(f"your body weight is: {body_weight} lbs, and the equivalent in kgs is: {rounded_weight} ")
# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.

num = int(input("Please enter a number between 1-100 : "))
if (num % 2) == 0:
   print("user_number is Even")
else:
   print("user_number is Odd")
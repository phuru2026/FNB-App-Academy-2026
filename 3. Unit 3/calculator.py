#using float(input()) to collect 2 numbers from user
number1= float(input("Please enter the 1st number: "))
number2= float(input("Please enter the 2nd number: "))

#calculating and displaying all results rounded off to 2 decimal place using round
addition=  round(number1 + number2, 2)
print(addition)
subtraction= round(number1 - number2, 2)
print(subtraction)
multiplication= round(number1 * number2, 2)
print(multiplication)

#handle division by zero
if number2 !=0:
    division= round(number1 / number2, 2)
    floor_division= round(number1 // number2, 2)
    modulus= round(number1 % number2, 2)
else:
     division= 'Division by 0 not allowed!'
     floor_division= 'Floor d by 0 not allowed'
     modulus= 'Modulus by 0 not allowed'

#displaying all results in a formatted table using f-strings
print("\n================== Calculator ==================")
print(f"{'Operation':<25}{'Result':>15}")
print("-" * 42)
print(f"{'Addition (+)':<25}{addition:>15}")
print(f"{'Subtraction (-)':<25}{subtraction:>15}")
print(f"{'Multiplication (*)':<25}{multiplication:>15}")
print(f"{'Division (/)':<25}{division:>15}")
print(f"{'Floor Division (//)':<25}{floor_division:>15}")
print(f"{'Modulus (%)':<25}{modulus:>15}")
print("=" * 42)

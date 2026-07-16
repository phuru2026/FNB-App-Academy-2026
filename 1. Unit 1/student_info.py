#using input() to collect user information
full_name= input("Please enter your full name: ")
surname= input("Please enter your surname: ")
age= int(input("Please enter your age: "))
favourite_number= float(input("Please enter your favourite number: "))
#using the f string
fullname= print(f"Welcome, {full_name}! ")
#uppercase and title case
print(f"your name in uppercase is: {full_name.upper()} and your surname in title case is: {surname.title()}")
#calculating age in months
age_in_months= age * 12
print(f"Your age in months is: {age_in_months} months")
#rounding off my favourite number to 2 decimal places
rounded_off_to_2_decimal_places= round(favourite_number, 2)
print(f" Tour favourite number to 2 decimal places is: {rounded_off_to_2_decimal_places}")
#checking data types
print(f'fullname data type is: {type(full_name)}')
print(f'surname data type is: {type(surname)}')
print(f'age data type is: {type(age)}')
print(f'favourite_number data type is: {type(favourite_number)}')   
#asking the user to input their secret password using input
password= input('Enter your secret password: ')

#using .strip() to clean up any accidental spaces
user_password= password.strip()

#string indexing
first_letter= user_password[0]
last_letter= user_password[-1]

#printing a hint using an f-string that forces the letters into upperrcase
print(f'Hint: Your password starts with a {first_letter.upper()} and ends with a {last_letter.upper()}')
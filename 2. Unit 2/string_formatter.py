#collecting user's name, surname, bio using input()
first_name= input('Enter your first name: ')
last_name= input('Enter your last name: ')
short_bio= input('Provide a short bio of yourself:')

#creating a username by combining first initial + last name using lowercase()
user_name= f'{first_name[0].lower()}{last_name.lower()}'

#displaying fullname in title case()
full_name= f'{first_name} {last_name}'.title()

#removing leading/trailing whitespace from the bio before displaying using .strip()
clean_short_bio= short_bio.strip()


#counting and displaying the number of characters in the bio using len()
length= len(clean_short_bio)

#replacing any occurence of "I am" in the bio with "I'm"
new_short_bio= clean_short_bio.replace("I am", "I'm")

#displaying all output using the f-string
print("\n ========== User Profile==========")
print(f'Username: {user_name}')
print(f'User Fullname: {full_name}')
print(f'Short Bio: {new_short_bio}')
print(f'Bio length: {length}')
print("========== The End =================")
#collecting learner information
learner_name= input("Enter learner's name: ")
math= float(input("Enter your math mark: "))
economics= float(input("Enter your economics mark: "))
tech= float(input("Enter your tech mark: "))

#calculating the average of the 3 subjects
average= (math + economics+ tech)/3

#assigning a letter grade using if/elif/else
if average >= 80:
    grade= "A"
elif average >= 70:
    grade= "B"
elif average >= 60:
    grade= "C"
elif average >= 50:
    grade= "D"
else:
    grade= "F"

#assigning pass or fail status
if average >=50:
    status= "Pass"
else:
    status= "Fail"

#creating a report card
print("\n==================== Learner Report Card ====================")

print(f"{'Learner Name':<25}{learner_name:>15}")
print(f"{'Math':<25}{math:>15.2f}")
print(f"{'Economics':<25}{economics:>15.2f}")
print(f"{'Tech':<25}{tech:>15.2f}")

print(f"{'Average':<25}{average:>15.2f}")
print(f"{'Status':<25}{status:>15}")

print("\nClosing Remarks:")


print("\nIntervention Report:")

intervention = False

if math < 40:
    print("Math needs intervention.")
    intervention = True

if economics < 40:
    print("Economics needs intervention.")
    intervention = True

if tech < 40:
    print("Tech needs intervention.")
    intervention = True

if not intervention:
    print("Well done!!!")

print("=" * 61)




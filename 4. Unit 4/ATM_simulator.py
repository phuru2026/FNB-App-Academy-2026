#setting a fixed variable
balance= 500

#request the amount the user wants to withdraw using the float()
amount= float(input("Enter withdrawal amount(R) "))

#using the if() statement to set conditions
if amount <= 0:
    message= "Invalid amount. You must withdraw more than R0."

elif amount <= balance:
    balance = balance - amount
    message= "Withdrawal successful!"
else:
    message= "Declined!! Insufficient funds!!"

#ATM slip
print("\n==================ATM SLIP==================")
print(f"{'Withdrawal amount(R)':<25}{amount:>15.2f}")
print(f"{'Remaining amount(R)':<25}{balance:15}")

print(f"{'Status':<25}{message:>15}")

print("=================Thank You!!!=================")
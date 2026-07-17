#collecting driving information
desired_kilometers= float(input("Enter how many kilometers you want to drive: "))
petrol_price= float(input("Enter the current petrol price: R "))
litre_usage= desired_kilometers / 10

#calculating total cost of petrol needed
total_cost= litre_usage * petrol_price

print("\n==================== Travelling Costs ===================")

print(f"{'Distance':<25}{desired_kilometers:>15}")
print(f"{'Petrol Price per litre (R)' :<25}{petrol_price:>15.2f}")
print(f"{'Litres needed':<25}{round(litre_usage, 2):>15}")
print(f"{'Travelling Costs (R)':<25}{round(total_cost, 2):>15}")

print("="*58)
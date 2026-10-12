salary = float(input("Enter your salary: "))
raisePercentage = float(input("Enter the raise percentage: "))
raiseAmount = salary * (raisePercentage / 100)
newSalary = salary + raiseAmount
print(f"Your new salary after a {raisePercentage}% raise is: {newSalary:.2f}")
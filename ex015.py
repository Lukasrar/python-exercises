valuePerDay = 60
valuePerKm = 0.15

daysUsed = int(input("Enter the number of days the car was used: "))
kmDriven = float(input("Enter the number of kilometers driven: "))

totalCost = (daysUsed * valuePerDay) + (kmDriven * valuePerKm)
print(f"The total cost of renting the car is: ${totalCost:.2f}")
number = int(input("Enter a number: "))

print(f"analysis of the number {number}:")
print(f"Units: {number % 10}")
print(f"Tens: {(number // 10) % 10}")
print(f"Hundreds: {(number // 100) % 10}")
print(f"Thousands: {(number // 1000) % 10}")
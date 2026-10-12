value = int(input("Enter a number: "))
multipliers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for multiplier in multipliers:
    result = value * multiplier
    print(f'{value} x {multiplier} = {result}')
    
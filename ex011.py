wallWidth = float(input('Enter the width of the wall in meters: '))
wallHeight = float(input('Enter the height of the wall in meters: '))
wallArea = wallWidth * wallHeight
paintCoverage = 2
paintNeeded = wallArea / paintCoverage
print(f'The area of the wall is {wallArea:.2f} square meters.')
print(f'The amount of paint needed to cover the wall is {paintNeeded:.2f} liters.')

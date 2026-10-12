valueOfTheProduct = float(input('Enter the value of the product: R$'))
discountPercentage = float(input('Enter the discount percentage: '))
discountAmount = valueOfTheProduct * (discountPercentage / 100)
finalPrice = valueOfTheProduct - discountAmount
print(f'The discount amount is R${discountAmount:.2f}')
print(f'The final price after discount is R${finalPrice:.2f}')
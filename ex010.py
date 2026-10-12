value = float(input("Enter a value in brazilian reais: R$"))
dollarValue = 5.25

dollarAmount = value / dollarValue

print(f'you can buy {dollarAmount:.2f} dollars with {value:.2f} reais')
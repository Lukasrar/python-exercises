from random import choice

firstStudent = input("Enter the name of the first student: ")
secondStudent = input("Enter the name of the second student: ")
thirdStudent = input("Enter the name of the third student: ")
fourthStudent = input("Enter the name of the fourth student: ")


students = [firstStudent, secondStudent, thirdStudent, fourthStudent]

chosenStudent = choice(students)


print(""f"The chosen student is: {chosenStudent}")
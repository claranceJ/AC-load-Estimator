# Write your AC Load Estimator solution here

#code to prompt user to enter width
width = float(input("Please Enter the width: "))

#code to prompt user to enter height
height = float(input("Please Enter height: "))

#code to prompt user to enter number_of_people
number_of_people = int(input("Please Enter number of people: "))

#formular for horsepower
horsepower = width * height * 0.1 + number_of_people * 0.06

print(f"the total horsepower is {horsepower:.2f}hp")

txt = "Calculator"

x = txt.center(40, " ")

print(x)
num1= float(input("enter first number: "))
num2= float(input("enter second number"))

print("Select an operation: ")
print("1- Addition")
print("2- Subtraction")
print("3- Multiplication")
print("4- Division")

choice = float(input("Enter your choice(1-4): "))

if choice == 1:
    result = num1 + num2
    print("The result is - ", result)
elif choice == 2:
    result = num1 - num2
    print ("The result is - ",result)
elif choice == 3:
    result = num1 * num2 
    print("The result is- ",result)
elif choice== 4:
    result =  num1 / num2
    print("The result is- ",result)
else:
    print("Invalid input. Try again.")



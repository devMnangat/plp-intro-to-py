# basic calculator program

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

operator = input("Enter an operation(1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operator == '1':
    result = num1 + num2
    print(round(result,2))

elif operator == "2":
    result = num1 - num2
    print(round(result,2))

elif operator == "3":
    result = num1 * num2
    print(round(result,2))

elif operator == "4":
    result = num1 / num2
    print(round(result,2))

else:
    print(f"{operator} is not a valid operator")

# age = int(input("enter your age: "))
# if age >= 100:
#     print("you are too old to sign up")
# elif age >= 16:
#     print("you are eligible to sign up")
# elif age < 0 :  
#     print("invalid age")
#     
# else: print("you are NOT eligible to sign up ur age is too low")

op = input("enter an op (+  -  *  /): ")
num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))

if op == "+":
    result = num1 + num2
    print(result)
elif op == "-":
    result = num1 - num2
    print(result)
elif op == "*":
    result = num1 * num2
    print(result)
elif op == "/":
    result = num1 / num2
    print(result)
else:
    print(f"{op} is a invalid operator")
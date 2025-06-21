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

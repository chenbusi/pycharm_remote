a = int(input("enter first number: "))
b = int(input("enter second number: "))

try:
    result = a / b
    print(result)
except ZeroDivisionError as e:
    print(f"oops {e.args}")
print("OK")

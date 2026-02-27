def basic_math_list(a, b):
    results = [a + b , a - b , a * b , a / b]
    return results

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = basic_math_list(num1, num2)
print(result)
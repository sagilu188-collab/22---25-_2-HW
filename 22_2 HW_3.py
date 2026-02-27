import random


def get_random_between_1_10() -> int:

    return random.randint(1, 10)



def get_random_operation() -> str:

    operations = ['+', '-', '*', '%']
    return random.choice(operations)



def calc_result(num1: int, oper: str, num2: int) -> int:

    if oper == '+':
        return num1 + num2
    elif oper == '-':
        return num1 - num2
    elif oper == '*':
        return num1 * num2
    elif oper == '%':
        return num1 % num2



num1 = get_random_between_1_10()
oper = get_random_operation()
num2 = get_random_between_1_10()
result = calc_result(num1, oper, num2)

print(f"{num1} {oper} {num2} = ?")
user_result = int(input('whats the result? '))

if result == user_result:
    print('Correct!')
else:
    print(f"Wrong.. the answer was {result}")
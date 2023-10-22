#!/usr/bin/python3
import os


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


opr_func = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
        }


def calculator():
    num1 = float(input("Enter First number: "))
    for symbol in opr_func:
        print(symbol)

    flag = True
    while flag:
        opr_symbol = input("Pick an operation: ")
        num2 = float(input("Enter Second number: "))
        cal_func = opr_func[opr_symbol]
        output = cal_func(num1, num2)
        print(f"{num1} {opr_symbol} {num2} = {output}")

        more = input(f"Enter 'y' to continue calculation with {output} or 'n' to start new calculation or 'x' to exit: ").lower()
        if more == 'y':
            num1 = output
        elif more == 'n':
            flag = False
            os.system('cls')
            calculator()
        else:
            flag = False


calculator()

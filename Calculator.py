def math_Calculator(a,b,op):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    elif op == '/':
        return a/b
    elif op == '%':
        return a%b
    elif op == '//':
        return a//b
    else:
        print("Invalid Operand")
a = int(input())
b = int(input())
op = input()
print(math_Calculator(a,b,op))
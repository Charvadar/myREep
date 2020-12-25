from datetime import datetime

def operation(val):
    operations = {
        'add': '+',
        'sub': '-',
        'mul': '*',
        'div': '/'
        }
    for key, value in operations.items():
        if val == key or val == value:
            return value
    return 0


def isValid(val):
    if val == '': return False
    vals = val.split()
    for v in vals:  
        if operation(v) == 0 and not v.replace('.','',1).isdigit():
            return False
        else:
            return True


def calculate(operator, operand1, operand2):
    operator = operation(operator)
    if operator == '+':
        return float(operand1) + float(operand2)
    elif operator == '-':
        return float(operand1) - float(operand2)
    elif operator == '*':
        return float(operand1) * float(operand2)
    elif operator == '/':
        return float(operand1) / float(operand2)


def getResult(inpt):
    vals = inpt.split()
    midPos = len(vals)//2
    result = vals[midPos]
    for i in range(1, midPos + 1):
        result = calculate(vals[midPos - i], result, vals[midPos + i])
    return result


def success(inpt, res):
    print("Expression: ", inpt)
    print("Result: ", res)
    print("Report: INFO-1, ERROR-0")
    with open("log.txt", "w") as f:        
        f.write(str(datetime.now()) + " ::  INFO :: " + inpt + str(res))


def failure(inpt):
    print("Expression: ", inpt)
    print("ERROR: Invalid expression")
    print("Report: INFO-1, ERROR-1")
    with open("log.txt", "w") as f:        
        f.write(str(datetime.now()) + " ::  ERROR :: Wrong input" + str(res))


def mainFunc():
    print("Welcome to Polish calculator")
    while True:
        inpt = input("Input the expression to get result or 'z' to exit:")
        if inpt == "z":
            print("Hope you enjoyed it :)")
            break
        if isValid(inpt):
            success(inpt, getResult(inpt))
        else:
            failure(inpt)


mainFunc()

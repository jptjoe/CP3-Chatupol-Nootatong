def Mathematical_operations(FirstNum, Operator, LastNum):
    if (Operator == "+"):
        print("=" , FirstNum + LastNum)
    elif (Operator == "-"):
        print("=" ,FirstNum - LastNum)
    elif (Operator == "*"):
        print("=" ,FirstNum * LastNum)
    elif (Operator == "/"):
        print("=" ,FirstNum / LastNum)
    else:
        print("Mathematical mark incorrect ")
num1 = int(input("Please enter first number :"))
MathMark = str(input("Please enter + or - or / or * :"))
num2 = int(input("Please enter last number :"))
Mathematical_operations(num1, MathMark, num2)
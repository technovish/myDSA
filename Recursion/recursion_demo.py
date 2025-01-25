def recursion(value):
    if value < 1:
        print("Value is less than 1")
    else:
        recursion(value-1)
        print(value)

recursion(5)
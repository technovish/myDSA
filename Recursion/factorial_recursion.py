def factorial(value):
    assert value >= 0 and int(value) == value, 'Does not satisfy condition'
    if value == 0:
        return 1
    else:
        return value * factorial(value-1)

print(factorial(10))
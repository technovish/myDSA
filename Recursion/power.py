def power(base: int, exp: int) -> int:
    assert exp>=0 and int(exp) == exp, 'Insert positive number'
    if exp == 1:
        return base
    else:
        return base * power(base, exp-1)
    
print(power(10,4))
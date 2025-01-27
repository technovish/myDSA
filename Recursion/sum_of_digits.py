def sum_digit(num):
    assert num>=0 and int(num) == num, 'Insert positive number'
    if num == 0:
        return 0
    else:
        return int(num%10) + sum_digit(int(round(num/10)))
    

print(sum_digit(112))
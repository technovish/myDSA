def max_key_value(dic):
    return max(dic,key=dic.get)

dict1 = {'a': 1, 'b': 5, 'c': 3}
print(max_key_value(dict1))

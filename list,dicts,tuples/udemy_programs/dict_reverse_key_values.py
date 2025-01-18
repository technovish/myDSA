def reverse_key_value(dic):
    new_dic = {}
    key = []
    value = []
    for k in dic.keys():
        key.append(k)
    for j in dic.values():
        value.append((j))

    for i in range(len(key)):
        new_dic[value[i]] = key[i]

    return new_dic

def reverse_dict(dic):
    return {v:k for k,v in dic.items()}

dict = {'a': 1, 'b': 5, 'c': 3}
print(reverse_key_value(dict))
print(reverse_dict(dict))
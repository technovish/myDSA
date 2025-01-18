'''Common Keys
Define a function with takes two dictionaries as parameters and merge them and sum the values of common keys.

Example:

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
merge_dicts(dict1, dict2)
Output:

{'a': 1, 'b': 5, 'c': 7, 'd': 5}'''

def commkeys(dic1, dic2):
    newdic = dic1.copy()
    for key,value in dic2.items():
            newdic[key] = newdic.get(key, 0) + value

    return newdic


dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
print(commkeys(dict1, dict2))

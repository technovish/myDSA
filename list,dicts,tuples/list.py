py_lists = ["Hello", 1, 2, 3.2, ['World'], 'Dabadoo']
int_lists = [1, 2, 3, 4, 5, 6, 7, 8, 9]

empty_list = []
for i in range(len(py_lists)):
  empty_list.append(py_lists[i])


# Method 1: Using slicing
reversed_list = py_lists[::-1]
##print(reversed_list)

py_lists.insert(0, 'ABCD')
#print(py_lists)
j=2
for j in range(len(int_lists)-1):
  print(int_lists[j])



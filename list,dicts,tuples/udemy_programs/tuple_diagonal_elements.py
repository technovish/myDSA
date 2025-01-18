input_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

def get_elements(input_tuple):
    lst = []
    for i in range(len(input_tuple)):
        for j in range(len(input_tuple[i])):
            if i==j:
                lst.append(input_tuple[i][j])
                continue
            else:
                continue
    print(lst)

def get_elements2(input_tuple):
    return tuple(input_tuple[i][i] for i in range(len(input_tuple)))

#get_elements(input_tuple)
print(get_elements2(input_tuple))
                
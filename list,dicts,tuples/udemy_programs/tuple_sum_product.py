tuple = (1,2,3,4)


def prod_sum(tuple):
    product = 1
    print("Sum:", sum(tuple))
    for i in range(len(tuple)):
        product *= tuple[i]
        
    print("Product:",product)

prod_sum(tuple)


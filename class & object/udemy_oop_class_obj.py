class StarCookie:
    def __init__(self):
        self.weight = input("Enter Weight: ")
        self.color = input("Enter Color: ")
        self.shape = input("Enter Shape: ")
    
    def print_attr(self):
        print(self.weight)
        print(self.color)
        print(self.shape)

cookie1 = StarCookie()

#prints all atrributes
print(cookie1.__dict__)
cookie1.print_attr()
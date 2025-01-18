my_file = open("text.txt", "w")
my_file.write("I'm the first line of the file!" + '\n' + "I'm the second line." + '\n' + "Third line here, boss.")
my_file.close()

my_file = open('text.txt', "r")
print (my_file.readline())
print (my_file.readline())
print (my_file.readline())
my_file.close()
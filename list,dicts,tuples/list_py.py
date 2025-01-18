list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 456]
print (list) #Prints complete list
print (list[0]) #Prints first element of the list
print (list[1:3]) #Prints elements starting from 2nd till 3rd
print (list[2:]) #Prints elements starting from 3rd element
print (tinylist * 2) #Prints list two times
print (list + tinylist)  #concatnation

list[2]=1.10  #updating list elements
print (list)

del list[4] #deleting list elements
print (list)

print (len(list)) #shows length of list

print (max(tinylist)) #prints maximum value in list

list.append(2009) #appends the list
print (list)

print (list.count(2009)) #counts the elements repeatition

list.extend(tinylist) #extends another list
print (list)

print (list.index(2009)) #prints the index no. of element

list.insert(3,1000)
print (list)

list.pop(3) #removes the element form list
print (list)

list.remove(786)
print(list)

list.reverse();
print(list)
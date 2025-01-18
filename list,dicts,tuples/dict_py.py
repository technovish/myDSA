dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print (dict['one']) # Prints value for 'one' key
print (dict[2]) # Prints value for 2 key
print (tinydict) # Prints complete dictionary
print (tinydict.keys()) # Prints all the keys
print (tinydict.values()) # Prints all the values

tinydict['code']=1234
print(tinydict)

tinydict.clear() #clear all entries from dictionary
print(tinydict)

del tinydict #delete dictionary

dict = {'name':'vishal', 'age':'30', 'address':"india", 'location':'bangalore'}
print(dict)
new_dict = dict.copy() #copy dictionary
print(new_dict)
dict2 = {}.fromkeys([1,2,3], None)
print(dict2)

print(dict.get('age')) #gets the value of the key
print(dict.setdefault('Job','Medallia')) #returns value of the if present else it will add a new key and set its value from default value 
print(dict)
dict.pop('location')
dict.update(dict2) #adds elements from 2nd dictionary to first one
print(dict)

#dictionary functions

print("Job" in dict) #checks key in dictionary
print("Medallia" in dict.values()) #checks values in dictionary
print("techno" not in dict.values())
print(len(dict)) #returns number of pairs in dict

#dictionary comprehension
list = ['Paris', 'London', 'Delhi', 'Dubai', 'Las Vegas', 'Berlin']
import random

num_dict = {num:random.randint(100,200) for num in list}
print(num_dict)

temprature = {kys:valu for (kys,valu) in num_dict.items() if valu < 150}
print(temprature)
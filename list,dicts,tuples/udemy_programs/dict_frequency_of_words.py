def count_word_frequency(lst):
    count = 0
    fruits = {}
    for i in lst:
        c = lst.count(i)
        fruits[i] = c
    print(fruits)

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
count_word_frequency(words) 


# {'apple': 3, 'orange': 2, 'banana': 1}

def count_word_frequency(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
print(count_word_frequency(words))
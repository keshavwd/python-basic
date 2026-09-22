#https://pynative.com/intermediate-python-exercises/
#List Comprehension Mastery
'''
words = ["apple", "bat", "cherry", "dog", "elderberry"]
li = []
for w in words:
    #i = len(words[w])
    if len(w)< 4:
        continue
    else:
        li.append(w.upper())
print(li)
'''

#Dictionary Merging with Logic
dict_a = {'a': 10, 'b': 20}
dict_b = {'b': 5, 'c': 15}
new_d = {}
for i in dict_a:
    new_d[i] = dict_a[i]
for j in dict_b:
    if j in new_d:
        new_d[j] = new_d[j]+dict_b[j]
    else:
        new_d[j] = dict_b[j]
print(new_d)

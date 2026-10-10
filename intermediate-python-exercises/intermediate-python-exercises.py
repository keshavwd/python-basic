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
'''
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
'''

#Frequency Map with Counter
'''
from collections import Counter
text = "Python Programming"
text = text.lower().replace(" ","")
res =  Counter(text)
print(res)
def counttxt(txt):
    ctxt = txt.lower().replace(" ","")
    return Counter(ctxt)
c = counttxt(text)
print(c)
'''

#Anagram Checker
'''
word1 = "listenss"
word2 = "silent"
word1 = sorted(word1)
word2 = sorted(word2)
if word1 == word2:
    print("Words are identical")
else:
    print("Words are not identical")
    print(word1, word2)
'''

#Flatten a Nested List
'''
nested = [1, [2, 3], [4, [5, 6]], 7]
nlist = []
for i in nested:
    print(i)
'''
#test
'''
i = 349
while i <= 7:
    print(i)
    i = i+1
    if i == 4:
        continue
'''
i = 153
li = 0
while i > 0:
    a = i%10
    #print(a)
    li = li + a**3
    i = i//10
    #print(i)
print(li)

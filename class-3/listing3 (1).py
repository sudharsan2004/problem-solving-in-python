import math 
#composite 
#Number of Words formed form the word "composite" is 9!/2!
word = input("Enter the Word: ")
word_list = list(word)
word_list.sort()
new_list = []
prev = word_list[0]
new_list.append(prev)
for current in word_list[1:]: 
    if prev != current: 
        new_list.append(current)
    prev = current 

print(new_list)
n = len(word_list)
res = math.factorial(n)
for i in new_list: 
    print(word_list.count(i))
    res = res/math.factorial(word_list.count(i))

print("Number of words formed form the word %s"%word,  res)
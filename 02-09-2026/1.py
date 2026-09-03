# write a python program to take a word and count the number of vowels a,e,i,o,u.

word = input("Enter word: ")
count = 0

for i in word:
    count += i in "aeiou"

print(count)
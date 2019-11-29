from typing import List, Any

word = input("enter a word to check if its a palindrome?")
word1 = list(word)
word1 = [ch for ch in word1]
word2 = list(word1)
word2.reverse()

for x in word1:
    if word1 == word2:
        print(" It is a palindrome")
        break
else:
    print("Not a palindrome")

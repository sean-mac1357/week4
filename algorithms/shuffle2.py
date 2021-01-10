import random

array = []
print("Enter a word to be shuffled\n")
word = input()
for index, char in enumerate(word):
    array.append(index)
print(array)


string = list(word)
random.shuffle(string)
print("\nThis is the shuffled up word\n")
print(''.join(string))

# print the new array containing the letters indices
# in relation to the shuffled word.
print(array)
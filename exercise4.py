# Write a Python function that takes a sentence and returns the number of vowels in it (ignore case).
def num_vowels(sentence):
    vowels = ["a", "e", "i", "o", "u"]; num_vowels = 0
    for letter in sentence.lower():
        if letter in vowels:
            num_vowels += 1
    return num_vowels
print(num_vowels("fOur vowEls"))
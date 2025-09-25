# Write a function that takes a list of words and returns the longest word.
def longest_word(word_list):
    longest_words = [""]
    for word in word_list:
        if len(word) > len(longest_words[0]):
            longest_words = [word]
        elif len(word) == len(longest_words[0]):
            longest_words.append(word)
    return longest_words
print(longest_word(["branch", "heat", "dying", "jerrry", "amongu"]))
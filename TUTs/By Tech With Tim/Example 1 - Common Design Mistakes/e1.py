# Example 1 - Common Design Mistakes

# Program Goal, print a list of words delimited by commas

# Solution 1 - What's wrong?
list_of_words = ["hello", "yes", "goodbye", "last", "hello"]
print(list_of_words[0] + "," + list_of_words[1] + "," + list_of_words[2] + "," + list_of_words[3])
# > Adding items to the list will break the code i.e not all elements will be printed
# > What if we are to change the delimiter? You'd have to change everywhere
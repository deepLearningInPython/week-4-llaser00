import numpy as np

# Follow the tasks below to practice basic Python concepts.
# Write your code in between the dashed lines.
# Don't import additional packages. Numpy suffices.

# [A] List Comprehensions and String Manipulation: Tokenization
#     Objective: Practice list comprehensions and basic string operations: split a sentence 
#                into individual words and use list comprehensions to make the code cleaner 
#                and more readable.

# List comprehension provides a concise way to create lists by embedding a for-loop inside 
# square brackets.
# Syntax: [expression for item in iterable if condition] (condition is optional).
# Example: squares = [x**2 for x in range(10) if x % 2 == 0]

# Large language models work with "tokens," which are the basic units of text (often words or subwords). 
# Tokenization is the process of breaking down sentences into these tokens. In this exercise, you’ll 
# create a simple tokenizer to split a sentence into words and remove punctuation.



# Task 1: Given a paragraph of text, implement a simple "tokenizer" that splits the paragraph 
#   into individual words (tokens) and removes any punctuation. Implement this using a list 
#   comprehension.

# Your code here:
# -----------------------------------------------
text = "The quick brown fox jumps over the lazy dog!"

# Write a list comprehension to tokenize the text and remove punctuation
clean = ''.join([char for char in text if char not in string.punctuation])
tokens = [clean.split() for word in clean]

# Expected output: ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
print(tokens)
# -----------------------------------------------

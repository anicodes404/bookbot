# Function below opens, reads and then counts and returns the number of words in the file.
def count_words():
    with open('./books/frankenstein.txt', 'r') as file: 
        content = file.read()
        words = content.split()
        length_words = len(words)
        print(f'{length_words} words found in the document')

count_words()
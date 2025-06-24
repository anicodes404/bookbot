from stats import count_words

# Function below opens, reads and returns the file.
def get_book_text():
    with open('./books/frankenstein.txt', 'r') as file: 
        content = file.read()
        print(content)






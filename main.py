# def get_book_text():
#     with open('./books/frankenstein.txt', 'r') as file: 
#         content = file.read()
#         print(content)

def count_words():
    with open('./books/frankenstein.txt', 'r') as file: 
        content = file.read()
        words = content.split()
        length_words = len(words)
        print(f'{length_words} words found in the document')

count_words()




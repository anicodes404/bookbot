def get_book_text():
    with open('./books/frankenstein.txt', 'r') as file: 
        content = file.read()
        print(content)

get_book_text()




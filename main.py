def get_book_text(file_path):
    with open(file_path, "r") as file: 
        file_contents = file.read()
    return file_contents


if __name__ == "__main__":
    path = "./books/frankenstein.txt"
    print(get_book_text(path))
import sys
from pathlib import Path

from stats import (
    get_num_words, 
    chars_dict_to_sorted_list, 
    get_chars_dict, 
)



def main(): 
    #  Checks if user enters a filename
    if len(sys.argv) < 2: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = Path(sys.argv[1])

    if not file_path.exists() or not file_path.is_file():
        print(f"Error: file not found or not a file: {file_path}")
        sys.exit(2)


    text = get_book_text(file_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print_report(file_path, num_words, chars_sorted_list)

def get_book_text(path):
    with open(path, 'r') as f: 
        return f.read()
    
def print_report(file_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
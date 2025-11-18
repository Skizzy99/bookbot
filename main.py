from stats import get_word_count
from stats import get_count_by_character
from stats import get_sorted_dicts
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as path_to_file:
        book_content = path_to_file.read()
        return book_content



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")

    

    content = get_book_text(sys.argv[1])

    word_count = get_word_count(content)
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    char_dict = get_count_by_character(content)
    # print(char_dict)

    sorted_dicts = get_sorted_dicts(char_dict)
    for sorted_dict in sorted_dicts:
        if(sorted_dict["char"].isalpha()):
            print(sorted_dict["char"] + ": " + str(sorted_dict["num"]))
        else:
            continue

    print("============= END ===============")
main()
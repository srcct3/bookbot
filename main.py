from stats import get_num_words, get_num_chars, set_letter_count_num
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]
    text = get_book_text(path_to_file)
    num_words = get_num_words(text)
    num_char = get_num_chars(text)
    num_char_list = set_letter_count_num(num_char)
    print_report(path_to_file, num_words, num_char_list)

def print_report(path_to_file, word_count, char_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in char_list:
        char = item["char"]
        count = item["num"]
        print(f"{char}: {count}")
    print("============= END ===============")

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        contnet = f.read()
        return contnet


main()

import sys
from stats import (count_words, total_count, count_characters)

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]

    text = read_book(path) 
    characters = list(text.lower())
    word_count = count_words(text)
    char_count = count_characters(characters)
    char_sorted = sort_characters(char_count)
    print_report_simple(path, word_count, char_sorted)


def print_report_simple(path, word_count, char_sorted):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in char_sorted:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

def print_report(path, word_count, char_sorted):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    print()

    for item in char_sorted:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def read_book(path):
    with open(path) as f:
        file_contents = f.read()
        return(file_contents)

def sort_on(d):
    return d["num"]

def sort_characters(char_count):
    sorted_list = []
    for ch in char_count:
        sorted_list.append({"char": ch, "num": char_count[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()
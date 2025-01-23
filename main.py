def main():
    path = "books/frankenstein.txt"
    text = read_book(path)
    characters = list(text.lower())
    word_count = count_words(text)
    char_count = count_characters(characters)
    char_sorted = sort_characters(char_count)

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

def count_words(text):
    words = len(text.split())
    return(words)

def total_count(characters):
    count = 0

    for c in characters:
        if c.isalpha() == True:
           count += 1
    return(count)

def count_characters(characters):
    count_dict = {}
    # print(characters)

    for c in characters:
        #if c.isalpha() == True:
            if c in count_dict:
                count_dict[c] += 1
            else:
                count_dict[c] = 1
    return(count_dict)

def sort_on(d):
    return d["num"]

def sort_characters(char_count):
    sorted_list = []
    for ch in char_count:
        sorted_list.append({"char": ch, "num": char_count[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()
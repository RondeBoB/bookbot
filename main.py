def read_book():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return(file_contents)

def count_words():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = len(file_contents.split())
        print(words)
    
count_words()
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
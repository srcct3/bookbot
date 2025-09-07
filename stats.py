def get_num_words(text):
    word_list = text.split()
    return len(word_list)

def get_num_chars(text):
    lower_case = text.lower()
    letter_count = {}
    for letter in lower_case:
        try:
            letter_count[letter] += 1
        except KeyError:
            letter_count[letter] = 1
    return letter_count

def set_letter_count_num(letter_count):
    new_list = []
    for key in letter_count:
        if key.isalpha():
            new_list.append({"char": key, "num": letter_count[key]})
    new_list.sort(reverse=True, key=sort_on)
    return new_list

def sort_on(items):
    return items["num"]

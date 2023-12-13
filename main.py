def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    count_letters(text)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_letters(text):
    sorted_keys = []
    key_array = []
    value_array = []
    char_dict = {}
    words = text.lower().split()
    for word in words:
        for char in word:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    for key in char_dict:
        if key.isalpha() == True:
            key_array.append(key)
            key_array.sort()
    for key in key_array:
        value_array.append(char_dict[key])
    for i in range(0, len(key_array)):
        print(f"The '{key_array[i]}' character was found {value_array[i]} times")


main()
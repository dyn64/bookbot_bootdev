def split_book_wide_open(book):
    return len(book.split())

def count_chars(book):
    full_count = {}
    for char in book:
        if char.isalpha():
            char = char.lower()
            if char not in full_count:
                full_count[char] = 1
            elif char in full_count:
                full_count[char] += 1
    return full_count

def sort_chars(char_dict):
    sorted_list = []
    for chars in char_dict:
        new_dict = {"char": chars, "num": char_dict[chars]}
        sorted_list.append(new_dict)
    sorted_list = sorted(sorted_list, key=lambda x: x['num'], reverse=True)
    return sorted_list

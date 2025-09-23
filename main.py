import sys

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8-sig') as file:
        return file.read()
    
from stats import split_book_wide_open, count_chars, sort_chars

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]

    book_contents = get_book_text(filepath)
    total_words = split_book_wide_open(book_contents)
    counted_book = count_chars(book_contents)
    #print(counted_book)

    # Printout
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    #print loop
    for entries in (sort_chars(counted_book)):
        print (f"{entries["char"]}: {entries["num"]}")

    print("============= END ===============")
main()
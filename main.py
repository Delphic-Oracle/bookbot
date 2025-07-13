from stats import get_wordcount, get_charcount, sort_charcount
import sys

def get_book_text(filepath):
    with open(filepath) as book:
        book_text = book.read()
        return book_text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_filepath = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_filepath}...")
    book = get_book_text(book_filepath)
    wordcount = get_wordcount(book)
    charcount = get_charcount(book)
    clean_charcount = sort_charcount(charcount)
    print("----------- Word Count ----------")
    print(f"Found {wordcount} total words")
    print("--------- Character Count -------")
    for char in clean_charcount:
        print(f"{char['char']}: {char['num']}")
    print("============= END ===============")


main()
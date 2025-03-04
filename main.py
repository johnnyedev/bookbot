import sys
from stats import get_word_count, get_char_count, sorted_counts, get_book_text


def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path to book>")
        sys.exit(1)
    else:
        # get book text
        file_path = sys.argv[1]
        book_text = get_book_text(file_path)
    
        # get count of words
        word_count = get_word_count(book_text)
    
        # get char count and sort desc
        char_count = get_char_count(book_text)
        sorted_chars = sorted_counts(char_count)

        # print output
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file_path[2::]}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
    
        for char in sorted_chars:
            print(f"{char}: {sorted_chars[char]}")

        print("============= END ===============")


main()

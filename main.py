import sys
from stats import (
    get_word_count,
    character_count,
    sort_count,
)

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path_to_file):
    try:
        with open(path_to_file, 'r') as f:
            file_contents = f.read()
            return file_contents
        
    except FileNotFoundError:
        print(f"File not found: {path_to_file}")
        return None
    
def main():
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    word_count = get_word_count(book_text)
    all_char = character_count(book_text)
    sort = sort_count(all_char)

    if book_text is not None:
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for item in sort:
            if not item["char"].isalpha():
                continue
            print(f"{item['char']}: {item['frequency']}")
        print("============= END ===============")

if __name__ == "__main__":
    main()
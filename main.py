from stats import get_word_count

def get_book_text(path_to_file):
    try:
        with open(path_to_file, 'r') as f:
            file_contents = f.read()
            return file_contents
        
    except FileNotFoundError:
        print(f"File not found: {path_to_file}")
        return None
    
def main():
    filepath = "/home/koreypatterson/workspace/github.com/bookbot/books/frankenstein.txt"
    book_text = get_book_text(filepath)
    word_count = get_word_count(book_text)

    if book_text is not None:
        print(f"{word_count} words found in the document")

if __name__ == "__main__":
    main()
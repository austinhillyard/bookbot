from stats import get_word_count, count_unique_characters, sort_counts
import sys

def get_book_text(file_path):
    with open(file_path) as file:
        file_contents = file.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    text = get_book_text(file_path)

    print("============ BOOKBOT ============\n" \
        f"Analyzing book found at {file_path}\n" \
        "----------- Word Count ----------\n" \
        f"Found {get_word_count(text)} total words\n" \
        "--------- Character Count -------\n")
    
    counts = count_unique_characters(text)
    sorted_counts = sort_counts(counts)
    for item in sorted_counts:
        print(f"{item[0]}: {item[1]}")

    print("============= END ===============")


main()
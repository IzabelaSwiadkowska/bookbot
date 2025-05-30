import sys
from stats import count_words
from stats import count_characters
from stats import get_book_text
from stats import dict_words
if len(sys.argv) !=2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)
book_path = sys.argv[1]

text = get_book_text(book_path)
result = count_words(text)
char_counts = count_characters(text)
print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
print("----------- Word Count ----------")
print(f"Found {result} total words")
print("--------- Character Count -------")
sorted_chars = dict_words(char_counts)
for items in sorted_chars:
    print(f"{items['char']}: {items['num']}")

print("============= END ===============")

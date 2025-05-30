
def get_book_text(file_path, encoding='utf-8'):
	with open(file_path) as f:
		story_lines =[]
		for line in f:
			new_line = line.lower()
			story_lines.append(new_line)

	return "".join(story_lines)

def main():
        path= sys.argv[1]
        book_text = get_book_text(path)
        count_words(book_text)



def count_words(text):
        words=text.split()
        num_words = len(words)
        return num_words

def count_characters(text):
	char_counts={}

	for char in text:
		low_char = char.lower()	
		if low_char.isalpha():
			if low_char in char_counts:
				char_counts[low_char]+=1
			else:
				char_counts[low_char]=1
	return char_counts

def dict_words(char_counts):
	new_dict=[]
	for key, value in char_counts.items():
		new_dict.append({"char":key, "num":value})
	new_dict.sort(key=sort_on, reverse=True)
	return new_dict

def sort_on(new_dict):
	return new_dict["num"]

	



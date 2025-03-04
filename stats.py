
def get_book_text(input_path):
    with open(input_path) as f:
        book_contents = f.read()
        return book_contents

def get_word_count(book_input):
    word_list = book_input.split()
    return len(word_list)


def get_char_count(book_input):
    lowercased_input = book_input.lower()
    char_dict = {}
    
    for char in lowercased_input:
        if char.isalpha():
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
    return char_dict


def sorted_counts(char_dict):
    sorted_values = dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_values
    
    





# Reads task6_read_me.txt and counts the number of words in it.
def count_words_in_file(file_path):
    file_path = 'task6_read_me.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        words = text.split()
        return len(words)

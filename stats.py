#This counts the words within the string of text

def get_word_count(text_string):
    counter = 0
    word_list = text_string.split()
    for word in word_list:
        counter = counter + 1
    return counter
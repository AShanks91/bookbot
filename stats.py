#This counts the words within the string of text

def get_word_count(text_string):
    counter = 0
    word_list = text_string.split()
    for word in word_list:
        counter = counter + 1
    return counter

def character_count(text_string):
    character_list = {}
    word_list = text_string.split()
    word_list = word_list.split()
    for c in word_list:
        character_list = c.lower()
        character_list[c.lower] +=1
    return character_list


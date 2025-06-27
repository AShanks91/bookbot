#This is the bookbot. 

filepath = "books/frankenstein.txt"
word_list = []
word = ""

#This reads the file and returns a string of text

def get_book_text(filepath):
    with open(filepath) as text:
        text_string = text.read()
    return text_string

text_string = get_book_text(filepath)

#This counts the words within the string of text
def get_word_count(text_string):
    counter = 0
    word_list = text_string.split()
    for word in word_list:
        counter = counter + 1
    return counter
    
def main():
    print(f"{get_word_count(text_string)} words found in the document")


main()
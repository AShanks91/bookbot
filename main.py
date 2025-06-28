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

from stats import get_word_count
from stats import character_count #TEST


def main():
    print(f"{get_word_count(text_string)} words found in the document") #fine
    print(f"{character_count}") #TEST
           
main()
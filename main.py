#This is the bookbot. 

path = "/books/frankenstein.txt"

#This reads the file


def get_book_text(f):
    with open(path) as f:
        text = f.read()
    return text

def main():
    print(get_book_text(""))

main()
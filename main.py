from stats import book_to_number, num_of_let, sort_of_dict
def get_book_text(book):
    with open(book) as file:
        file_contents = file.read()
        return file_contents
    


def main():

    print(num_of_let(get_book_text("books/frankenstein.txt")))

main()
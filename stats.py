def book_to_number(get_book_text):
    number = 0
    separate = get_book_text.split()
    for sep in separate:
            number += 1
    
    return number

def num_of_let(get_book_text):
    lowletter = {}
    cuttt = get_book_text.split()
    for cut in cuttt:
        small_cut = cut.lower()
        for smoll in small_cut:
            if smoll in lowletter:
                lowletter[smoll] += 1
            else:
                lowletter[smoll] = 1
    return lowletter

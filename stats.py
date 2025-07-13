def get_wordcount(book):
    words = book.split()
    wordcount = len(words)
    return wordcount

def get_charcount(book):
    charcount = {}
    for char in book:
        if char.lower() in charcount:
            charcount[char.lower()] += 1
        else:
            charcount[char.lower()] = 1
    return charcount

def sort_on(dict):
    return dict["num"]

def sort_charcount(charcount):
    dict_list = []
    for char in charcount:
        if char.isalpha():
            dict_list.append({"char": char, "num": charcount[char]})
    
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

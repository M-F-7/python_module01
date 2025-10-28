from curses.ascii import isdigit
import random


def generator(text, sep=" ", option=None):
    if isinstance(text, str) == False:
        raise TypeError("ERROR")
    if option != "shuffle" and option != "unique" and option != "ordered":
        if option != None:
            raise ValueError("ERROR")
    split:list = text.split(sep)
    tab:list = []
    if option == "shuffle":
        while split:
            word = random.randint(0, len(split) - 1)
            tab.append(split.pop(word))
    elif option == "unique":
        for word in split:
            if tab.index(word) == -1:
                continue
            tab.append(word)
    elif option == "ordered":
        tab = sorted(split)
    for word in tab:
        print(word)


def main():
    try:
        text = "Le Lorem Ipsum est simplement du faux texte."
        generator(text, option="unique")
    except (ValueError,TypeError) as e:
        print(e)

if __name__ == "__main__":
    main()
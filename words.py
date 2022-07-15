
def print_upper_words (array_of_words ) :
    """print out each word on a separate line, but in all uppercase. """
    for word in array_of_words:
        print (word.upper())


def print_upper_words_start_letter_e (array_of_words):
    """Change that function so that it only prints words that start with the letter ‘e’ (either upper or lowercase).
"""
    for word in array_of_words:
        if word.startswith ("e") or word.startswith ("E"):
            print (word.upper());


def print_upper_words2 (list_of_words, must_start_with) :
    """Make your function more general: you should be able to pass in a set of letters, and it only prints words that start with one of those letters.

For example:

# this should print "HELLO", "HEY", "YO", and "YES"

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})
"""
    for word in list_of_words:
        for letter in must_start_with:
            if (word.startswith (letter)):
                print (word.upper());
                break;

print_upper_words2(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})


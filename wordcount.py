from sys import argv


def count_words():
    script, filename = argv
    # open the file. open() returns a file object, not the contents
    w = open(filename)
    # contents = w.readline()
    # print contents
    
    # Creates the dictionary, "count" 
    # (word is the key, count/occurnences is the value)
    count = {}
   
    # scrub each line in the file
    # tokenize each word in a line

    for line in w:
        line = line.strip()
        words = line.split(' ')
        
        # for the new variable "word", in the list "words", 
        # we want to assign each as a key in our dictionary
        for word in words:
            # check to see if it already exists in the dictionary
            # if it does not exist in the dictionary, add it to the dictionary with a count of 1
            if count.get(word) == None:
                count[word] = 1
            # if it does exist in the dictionary, update the value to value + 1
            else:
                count[word] += 1

    # print count
    return count
    
def print_items(dictionary):
    # print the words and counts to the screen
    for word, count in dictionary.items():
        print word, count


def main():
    dictionary = count_words()
    print_items(dictionary)

if __name__ == "__main__":
    main()
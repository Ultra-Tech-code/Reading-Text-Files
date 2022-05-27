# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    file = open(filename)
    return file.read()


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    # split the test to string and saved in a list
    text_to_list = text.split()

    result = {}
    for i in range(len(text_to_list)):
        result[text_to_list[i]] = text_to_list.count(text_to_list[i])
    return result

# read_file_content("./story.txt")
print(count_words())
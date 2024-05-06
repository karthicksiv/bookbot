def main():
    path_to_file = "books/frankenstein.txt"
    contents = file_contents(path_to_file)
    print("-- Begin report of book/frankenstein.txt --")
    print(len(splitter(contents)), "words found in the document")
    char_dict = char_counter(contents)
    char_list = []
    for pair in char_dict:
        char_list.append({"char" : pair, "num" : char_dict[pair]})
    char_list.sort(reverse=True, key=sort_on)
    for i in char_list:
        print("The", i['char'], "character was found", i['num'], "times")

def sort_on(dict):
    return dict["num"]

def file_contents(path):
    with open(path) as f:
        contents = f.read()
    return contents

def splitter(contents):
    words = contents.split()
    return words

def char_counter(text):
    results = {}
    lower_text = text.lower()
    for char in lower_text:
        if char.isalpha():
            if not char in results:
                results[char] = 1
            else:
                results[char] = results[char] + 1
    return results

main()
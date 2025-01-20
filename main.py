print("--- Begin report of books/frankenstein.txt---")

def main():
    number_of_words = 0
    my_dictionary = {}
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()

        #counts words
        lines = file_contents.split()
        number_of_words += len(lines)
    print(f"{number_of_words} words found in the document")

    #processes characters
    lowered_file = file_contents.lower()
    filtered = [char for char in lowered_file if char.isalpha()] #keeping only the alphabetic characters
    for char in filtered:
        if char in my_dictionary:
            my_dictionary[char] += 1
        else:
            my_dictionary[char] = 1

    # sort and print        
    my_list = list(my_dictionary.items())
    my_list.sort(key=lambda item: item[1], reverse=True)
    for char, count in my_list:
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")

main()

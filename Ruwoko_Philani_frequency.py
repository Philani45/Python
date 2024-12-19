def build_dictionary(word_list):
    word_dict = {}
    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict

def main():
    input_text = input("Enter a text: ")
    # Tokenize the input text into words and convert them to lowercase
    words = input_text.lower().split()

    # Build the word frequency dictionary
    word_freq_dict = build_dictionary(words)

    # Sort the dictionary by keys (words)
    sorted_word_freq = sorted(word_freq_dict.items())

    # Display the bag of words
    for word, frequency in sorted_word_freq:
        print(f"{word}: {frequency}")

if __name__ == "__main__":
    main()

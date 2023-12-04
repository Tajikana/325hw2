import string


def eliminating(word_list):
    stop = set(["a", "an", "the"] + list(string.punctuation))
    new_list = [word for word in word_list if word.lower() not in stop]
    return new_list


def frequency(word_list):
    frequency_dict = {}
    for word in word_list:
        word_lower = word.lower()
        frequency_dict[word_lower] = frequency_dict.get(word_lower, 0) + 1
    return frequency_dict


def removedup(word_list):
    unique_list = []
    seen = set()
    for word in word_list:
        word_lower = word.lower()
        if word_lower not in seen:
            seen.add(word_lower)
            unique_list.append(word_lower)
    return unique_list


def three_word(word_list):
    return [word_list[i:i + 3] for i in range(0, len(word_list), 3)]


text = input("Enter your text: ")
words = text.split()

without_stop = eliminating(words)
print("The list without any stop word: ", without_stop)

frequencies = frequency(without_stop)
print("How many times each word repeats: ", frequencies)

unique = removedup(without_stop)
print("The list without any repeated words:", unique)

three = three_word(unique)
print("3-grams:", three)

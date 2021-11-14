# vowels: A, E, I, O, U
# consistent string = all letters same
# 1 second = can change a letter
# if chosen letter vowel, replace w/ consonant
# if consonant, replace w/ vowel

def solution(string: str):
    if string.count(string[0]) == len(string):
        return 0

    vowel_count = 0 + string.count("A") + string.count("E") + string.count("I") + string.count("O") + string.count("U")
    consonant_count = len(string) - vowel_count

    alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
     'X', 'Y', 'Z']
    info_list = []  # [['A', 1], ['B', 1], ['C', 1], ['D', 0],.....]
    for letter in alphabet_list:
        info_list.append([letter, string.count(letter)])

    unique_vowels = 0
    unique_consonants = 0
    for i in range(len(info_list)):
        if info_list[i][1] != 0:
            if info_list[i][0] in ["A", "E", "I", "O", "U"]:
                unique_vowels += 1
            else:
                unique_consonants += 1
    most_common_vowel = "A"
    most_common_vowel_num = string.count("A")
    vowel_list = ["A", "E", "I", "O", "U"]

    # Finding the most common vowel
    for i in range(1, len(vowel_list)):
        if string.count(vowel_list[i]) > most_common_vowel_num:
            most_common_vowel = vowel_list[i]
            most_common_vowel_num = string.count(vowel_list[i])

    # Finding the most common consonant
    most_common_consonant = "B"
    most_common_consonant_num = string.count("B")
    consonant_list = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    for i in range(1, len(consonant_list)):
        if string.count(consonant_list[i]) > most_common_consonant_num:
            most_common_consonant = consonant_list[i]
            most_common_consonant_num = string.count(most_common_consonant)

    changes_option_1 = 0

    # Option 1: Change vowels into consonants
    changes_option_1 += vowel_count + (consonant_count - most_common_consonant_num)
    changes_option_1 += (consonant_count - most_common_consonant_num)

    changes_option_2 = 0

    # Option 2: Change consonants into vowels
    changes_option_2 += consonant_count + (vowel_count - most_common_vowel_num)
    changes_option_2 += (vowel_count - most_common_vowel_num)

    if changes_option_2 < changes_option_1:
        return changes_option_2
    return changes_option_1



def get_input():
    test_cases = int(input())
    for i in range(test_cases):
        string = str(input())
        result = solution(string)
        print(f"Case #{i + 1}: {result}")


get_input()


word_1 = input()
word_2 = input()
length_of_the_word_1 = len(word_1)
length_of_the_word_2 = len(word_2)

if(length_of_the_word_1 == length_of_the_word_2):
    word_1 = sorted(word_1.lower())
    word_2 = sorted(word_2.lower())
    if (word_1 == word_2):
        print("Given Strings are anagrams")
    else:
        print("Given strings are not anagrams")


else:
    print("Given two strings are not Anagrams")
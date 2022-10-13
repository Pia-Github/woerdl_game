#you need the nltk library to run this. In case you don't have it, install it:
#pip install --user -U nltk

import nltk
nltk.download('words')

import random
import itertools

from nltk.corpus import words

word_list = words.words()

letter_count = set([])
for l in word_list:
    letter_count.add(len(l))

while True:
    selected_number = (input("Please enter the nuber of letters you'd like to guess: "))
    if  selected_number.isnumeric():
        selected_number = int(selected_number)

        if selected_number <= max(letter_count) and selected_number >= min(letter_count):
            print("Cool, you are going to guess a word with " + str(selected_number) + " letters")
            break

        elif selected_number > max(letter_count):
            print("There is no word with that many letters")

        elif selected_number < min(letter_count):
            print("You are stupid, try again")

    else:
        print("You can only enter a number")

words_right_count = [word.lower() for word in word_list if len(word) == selected_number]




mystring = ''
for x in words_right_count:
    mystring += ' ' + x
# mystring = mystring.lower()

new_list = list(mystring)

separated_letters = [list(v) for k,v in itertools.groupby(new_list,key=str.isspace) if not k]

selected_word = random.choice(separated_letters)
display_selected_word = ''
for x in selected_word:
    display_selected_word += ' ' + x

count = 0

while True:
    user_input = (input("Please enter a " + str(selected_number) + " letter word: "))
    user_input_list = list(user_input)
    user_output = [len(set(i)) == 1 for i in zip(selected_word, user_input_list)]
    user_output_new = []

    if len(user_input) == selected_number and user_input in words_right_count:
        count += 1
        if user_output.count(True) == len(user_output):
            print("Congratulations!!! You needed " + str(count) + " attempts")
            break
        elif count > 5:
            print("FAAAAAAAIIILLL! The correct word would have been " + display_selected_word)
            break
        elif count <= 5:
            for x, y, z in zip(selected_word, user_output, user_input_list):
                if y == True:
                    user_output_new.append("True")
                else:
                    if z in selected_word:
                        user_output_new.append("Existing")
                    else:
                        user_output_new.append("False")
            print(user_output_new)

    elif len(user_input) != selected_number:
        print("You idiot, are you not able to count?! You must enter exactly " + str(selected_number) + " letters")

    elif user_input not in words_right_count:
        print("You must enter an existing word")
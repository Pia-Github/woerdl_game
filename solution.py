# import packages (this is prework and is not necessary when it runs in parallel to the "questioning part". This is the same list as the questioning part works with)
import nltk
nltk.download('words')

import random
import itertools

from nltk.corpus import words

# create a word list from which to guess (this is prework and is not necessary when it runs in parallel to the "questioning part". This is the same list as the questioning part works with)

word_list = words.words()

letter_count = []
for l in word_list:
    letter_count.append(len(l))

word_len = {}
for key in word_list:
    for value in letter_count:
        word_len[key] = value
        letter_count.remove(value)
        break

# here you have to change the word lenght to the selected number of letters that are wanted to guess (here: 5)
words_right_count_pre = list({i for i in word_len if word_len[i] == 5})

words_right_count = []

for x in words_right_count_pre:
    words_right_count.append(x.lower())

mystring = ''
for x in words_right_count:
    mystring += ' ' + x

new_list = list(mystring)

# *separated_letters* is the first list we are working with

separated_letters = [list(v) for k, v in itertools.groupby(new_list, key=str.isspace) if not k]
len(separated_letters)


# DEFINE FUNCTIONS

# how often does letter appear in a selected word?
def count_in_word(x):
    ciw = {}
    for c in set(x):
        ciw[c] = x.count(c)
    return ciw


# get the count for each distinct letter
def check_freq(x):
    freq = {}
    for c in set(x):
        freq[c] = x.count(c)
    return freq


# count of each letter of one word: s = list it should take the words from; z = string of all words and letters; y = the letter that should be counted (iterable)
def counted_dict(s, z, y):
    word_dict = {i: 0 for i in (s[y])}
    final_dictionary = {x: (check_freq(z)).get(x, 0) + word_dict.get(x, 0)
                        for x in set(word_dict)}
    return final_dictionary


# set up funtion to calculate sum of a word
def returnSum(myDict):
    list = []
    for i in myDict:
        list.append(myDict[i])
    final = sum(list)

    return final


# calculate letter sum of one word without mulitplication: s = list it should take the words from; z = string of all words and letters; x = index of the word we want to ge t the sum from (iterable)
def sum_calc(s, z, x):
    dict_new = counted_dict(s, z, x)
    returnSum(dict_new)
    return returnSum(dict_new)


# create a dictionary out of a word that is on the list of possible to guess words
def word_dict(s, x):
    word_dict = {i: 0 for i in (s[x])}
    return word_dict


# this function gives feedback to every letter you enter based on the feedback that was given to the first trial word
def checkKey(key):
    if key in input_feedback.keys():
        return (input_feedback[key])
    else:
        return ("Not present")



# DEFINE THE POOL TO WORK WITH
available_list = separated_letters
available_string = mystring




#GUESS WORD

# sum of each word in a list
sum_list = []
for x in range(len(available_list)):
        sum_list.append(sum_calc(available_list, available_string, x))

# this is the first word you should guess
guess_list = available_list[sum_list.index(max(sum_list))]

guess_word = ""
for i in guess_list:
    guess_word += i
print ("The first word to guess is \"" + guess_word + "\"")




# define variables for next run (has to be added manually)
guessed_word = guess_list
feedback = ['False', 'False', 'False', 'False', 'True']



# combine user input with it's feedback in a string
input_feedback = {}
for key in guessed_word:
    for value in feedback:
        input_feedback[key] = value
        feedback.remove(value)
        break

#need to fix!!!
feedback = ['False', 'False', 'False', 'False', 'True']




# this is a list of all words with the right count as a dict
first_dict_list =[]
for x in range(len(available_list)):
        first_dict_list.append(word_dict(available_list, x))



#this is a list without words that contain letters that were reolied with "False"
second_list_1 = []
for y in first_dict_list:
    if any(checkKey(x) == 'False' for x in y):
        continue
    else:
        second_list_1.append(y)

print("first list: " + str(len(available_list)) + " items; second list: " + str(len(second_list_1)) + " items")




second_list_list = []

for x in second_list_1:
    second_list_list.append(list(x))




# only words that have "True" letters at the right position
second_list_2 = []

for x in second_list_list:
    if any ((x[y] != guessed_word[y] and feedback[y] == 'True') for y in range(len(x))):
            continue
    else:
        second_list_2.append(x)

len(second_list_2)





# this sorts out words that have either an existing letter not at all or they have it but at the wrong position

second_list_final = []

for x in second_list_2:
    if any ((x[y] == guessed_word[y] and feedback[y] == 'Existing') for y in range(len(x))):
            continue
    elif any ((feedback[y] == 'Existing' and guessed_word[y] not in second_list_2) for y in range(len(x))):
            continue
    else:
        second_list_final.append(x)

len(second_list_final)

# PREWORK
# Unlist second_list final
res = list(map(''.join, second_list_final))

# make the unlisted list to a string
available_string = ''
for x in res:
    available_string += ' ' + x

# DEFINE THE POOL TO WORK WITH
available_list = second_list_final
# available_string

# NOW RETURN TO "GUESS WORD"!
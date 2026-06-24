

# import packages (this is prework and is not necessary when it runs in parallel to the "questioning part". This is the same list as the questioning part works with). You only need to install wordfreq once. Watch out that the word_n_list is the same language and has the same number of words as in the game
#import wordfreq

import random
import itertools

from wordfreq import top_n_list

word_list = top_n_list("en", 50000)

#print (word_list[:10])

# create a word list from which to guess (this is prework and is not necessary when it runs in parallel to the "questioning part". This is the same list as the questioning part works with)

letter_count = []
for l in word_list:
    letter_count.append(len(l)) 
    
word_len = {}
for key in word_list:
    for value in letter_count:
        word_len[key] = value
        letter_count.remove(value)
        break

#here you have to change the word lenght to the selected number of letters that are wanted to guess (here: 4)
words_right_count_pre = list({i for i in word_len if word_len[i]== 4})

words_right_count = []

for x in words_right_count_pre:
    words_right_count.append(x.lower())


mystring = ''
for x in words_right_count:   
    mystring += ' ' + x

new_list = list(mystring)

#*separated_letters* is the first list we are working with

separated_letters = [list(v) for k,v in itertools.groupby(new_list,key=str.isspace) if not k]
len(separated_letters)

#print (new_list[:10]) 
#print (separated_letters[:10])

#DEFINE FUNCTIONS

# how often does letter appear in a selected word?
def count_in_word(x):
    ciw = {}
    for c in set(x):
       ciw[c] = x.count(c)
    return ciw

#get the count for each distinct letter
def check_freq(x):
    freq = {}
    for c in set(x):
       freq[c] = x.count(c)
    return freq

#count of each letter of one word: s = list it should take the words from; z = string of all words and letters; y = the letter that should be counted (iterable)
def counted_dict (s, z, y):
    word_dict = { i : 0 for i in (s[y]) }
    final_dictionary =  {x: (check_freq(z)).get(x, 0) + word_dict.get(x, 0)
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
def sum_calc (s, z, x):
    dict_new = counted_dict (s, z, x)
    returnSum(dict_new)
    return returnSum(dict_new)

# create a dictionary out of a word that is on the list of possible to guess words 
def word_dict (s, x):
    word_dict = { i : 0 for i in (s[x])}
    return word_dict

# this function gives feedback to every letter you enter based on the feedback that was given to the first trial word
def checkKey(key):
    if key in input_feedback.keys():
        return(input_feedback[key])
    else:
        return("Not present")

# DEFINE THE POOL TO WORK WITH
available_list = separated_letters
available_string = mystring

#print (available_list [:10])
#print (available_string[:10])
#print(set(len(x) for x in available_list))

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
feedback = ['False', 'Existing', 'True', 'False']
feedback_copy = list(feedback)
feedback_list = list(feedback)

#print (guess_word)
#print (feedback_copy)
#print (feedback_list)

#make the guessed word to a list
guess_word_list = list(guess_word)

#print(guess_word_list)
#print (feedback_list)

# combine user input with it's feedback in a string
input_feedback = {}
for key in guessed_word:
    for value in feedback_copy:
        input_feedback[key] = value
        feedback_copy.remove(value)
        break
        

#print (input_feedback)
#print (feedback_list)

#create a list of fobidden letters (letters marked as "False")

fobidden_letters = []
for x in input_feedback:
    if input_feedback[x] == 'False':
        fobidden_letters.append(x)
    else:
        continue
    
#print (fobidden_letters)

#delete all words with forbidden letters from the list

list_cleaning_false = []
for word in available_list:
    if any(letter in word for letter in fobidden_letters):
        continue
    else:
        list_cleaning_false.append(word)
        
#print(list_cleaning_false[:10])
#print(len(list_cleaning_false))

#delte all words, that have a letter different than the true one on the true position
position = []
for i in range(len(feedback_list)):
    if feedback_list[i] == "True":
        position.append(i)
        
list_cleaning_false_true = []
for word in list_cleaning_false:
    if all (word[i] == guess_word_list[i] for i in position):
        list_cleaning_false_true.append(word)
    else:
        continue
        


#print(list_cleaning_false_true[:10])
#print(len(list_cleaning_false_true))

#create a list of existing letters (meaning all letters that were marked as "Existing")

existing_letters = []
for x in input_feedback:
    if input_feedback[x] == 'Existing':
        existing_letters.append(x)
    else:
        continue
    
#print (existing_letters)

#delete words that don't contain all existing letters (meaning all letters that were marked as "Existing")

list_cleaning_false_true_existing_1 = []
for word in list_cleaning_false_true:
    if all (letter in word for letter in existing_letters):
        list_cleaning_false_true_existing_1.append(word)
    else:
        continue
        
#print(list_cleaning_false_true_existing_1[:10])
#print(len(list_cleaning_false_true_existing_1))

#delete words that contain the existing letter at the spot of the existing letter

position_existing = []
for i in range(len(feedback_list)):
    if feedback_list[i] == "Existing":
        position_existing.append(i)
        
list_cleaning_false_true_existing_2 = []
for word in list_cleaning_false_true_existing_1:
    if any (word[i] == guess_word_list[i] for i in position_existing):
        continue
    else:
        list_cleaning_false_true_existing_2.append(word)
        
#print(list_cleaning_false_true_existing_2[:10])
#print(len(list_cleaning_false_true_existing_1))

# DEFINE THE POOL TO WORK WITH in the next iteration

available_list = list_cleaning_false_true_existing_2

# NOW RETURN TO "GUESS WORD"!

#print(available_list[:10])
#print(len(available_list))





























import json
from difflib import get_close_matches
data = json.load(open('data.json'))


def translate(user_input):
    lower_word = user_input.lower()
    if lower_word in data:
        return data[lower_word]
    elif lower_word.title() in data:
        return data[lower_word.title()]
    elif lower_word.upper() in data:  # in case user enters words like USA or NATO
        return data[lower_word.upper()]
    elif len(get_close_matches(lower_word, data.keys())) > 0:
       ans = input("Did you mean %s instead? \nEnter yes or no " % get_close_matches(lower_word, data.keys())[0])
       lower_ans = ans.lower()
       if lower_ans == 'y' or lower_ans == 'yes':
            return data[get_close_matches(lower_word, data.keys())[0]]
       elif lower_ans == 'n' or lower_ans == 'n':
           return 'The word: ' + word + ' does not exist.\nPlease double check the word.'
       else:
           return 'I did not understand your entry'
    else:
        return 'The word: ' + word + ' does not exist.\nPlease double check the word.'


word = input("Enter Word: ")
output = translate(word)
if type(output) == list:
    for define in output:
        print(define)
else:
    print(output)
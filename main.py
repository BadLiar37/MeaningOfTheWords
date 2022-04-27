import json
from difflib import get_close_matches

data = json.load(open("092 data.json"))


def translate(our_word):
    our_word = our_word.lower()
    if our_word in data:
        return data[our_word]
    elif len(get_close_matches(our_word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes or N if no:" % get_close_matches(our_word, data.keys())[0])
        if yn == "y" or yn == "y":
            return data[get_close_matches(our_word, data.keys())[0]]
        elif yn == "N" or yn == "n":
            return "The word does not exist.Please double check it"
        else:
            return "Incorrect values"
    else:
        return "The word does not exist.Pleas,double check it"


word = input("Please input word:")
output=translate(word)
if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)



import difflib
from difflib import get_close_matches
import json

data = json.load(open("data.json", "r"))
def translate(word):
     return data[word]

capi = ""


while True:
    word = input(">> ").lower()
    if word in data:
        well = translate(word)
        for item in well:
            print(item)
            continue





    elif get_close_matches(word,data.keys(),cutoff=0.8):
        word2 = get_close_matches(word,data.keys(),cutoff=0.8)[0]
        word3 = str(get_close_matches(word,data.keys(),cutoff=0.8)[0]).upper()
        jojo = input("Did you mean "+ word3 + ",then press 'Y' for yes and 'N' for no: ").lower()

        if jojo == 'y':

            well2 = translate(word2)
            for item2 in well2:
                print(item2)




        else:
            print("The word doesn't exist.Please double check the word and try again ")
            continue


    else:
        print("The word doesn't exist.Please double check the word.  ")
        continue
    
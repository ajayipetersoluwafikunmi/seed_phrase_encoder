
#program to encode seed phrases
#this algorithm will be simple, just shift each character forward by two characters e.g a -> c and b -> d etc
#this simplicity comes with the inherent risk that it's easy to crack, 
#a list of all possible seedphrase words - 2048
#one foor loop and a few minutes to kill is all it'll take but here goes

import string

#  this algorithm should accept input
seed_phrase = input("enter seedphrase: ")
new_seed = ""

#and encode each word
alphabets = list(string.ascii_lowercase)
a_to_x = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x"]

for i in list(seed_phrase):
    if i in a_to_x:
        seed_phrase = list(seed_phrase)
        new_seed =  new_seed + alphabets[a_to_x.index(i) + 2]
    elif i == "y":
        new_seed = new_seed + "a"
    elif i == "z":
        new_seed = new_seed + "b"
    elif i == " ":
        new_seed = new_seed + " "
    else:
        pass
print(new_seed)

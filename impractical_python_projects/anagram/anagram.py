import load_dict

word_list = load_dict.load("../words.txt")

anagram_list = []

name = "Foster"
print("Inputname = {}".format (name))
name = name.lower()
print("Using name = {}".format(name))

name_sorted = sorted(name)
for word in word_list:
    word = word.lower()
    if word != name:
        if sorted(word) == name_sorted:
            anagram_list.append(word)

print()
if len(anagram_list) == 0:
    print("You need a larger dictionary or a new name!")
else:
    print("Anagrams =", *anagram_list, sep='\n')
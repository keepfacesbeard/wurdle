# create a test file
from io import FileIO
import json


filename = "sowpods.txt"

mod_list = []
count = 1
for line in FileIO(filename):
    # strip ending whitespaces including newline char
    line = line.rstrip()
    # concatenate every two lines
    if count % 2 == 0:
        mod_list.append(line)
    else:
        old_line = line
    count += 1


dict = []
for word in mod_list:
    if len(word) == 5:
        dict.append(word.upper())
##this is a scrabble dictionary?

# print(dict)


filename2 = "words_alpha.txt"

mod_list2 = []
count2 = 1
for line in FileIO(filename2):
    # strip ending whitespaces including newline char
    line = line.rstrip()
    # concatenate every two lines
    if count % 2 == 0:
        mod_list2.append(line)
    else:
        old_line = line
    count += 1


dict2 = []
for word in mod_list2:
    if len(word) == 5:
        dict2.append(word.upper())
##this is a scrabble dictionary?

# print(dict)

bigdict = dict2
for word in dict:
    if word in bigdict:
        continue
    else:
        bigdict.append(word)



# for word in sitedict:
#     if word in bigdict:
#         continue
#     else:
#         bigdict.append(word)



with open("dictionary.json") as ff:
    dictdata = json.load(ff)


biggestdict =[]
for key in dictdata:
    biggestdict.append(key.upper().encode('utf-8'))


finaldict = bigdict
for word in biggestdict:
    if len(word)==5:
        if word in finaldict:
            continue
        else:
            finaldict.append(word)
    else:
        continue

# print(len(finaldict))
print(finaldict)


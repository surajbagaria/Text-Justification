import sys
import re
'''
file = open("sample.txt")
print file.read()
'''
def special_words(charac,words, block_size): # this function will return list of words which need to be breaked in syllables
    s = []
    word_count = 0
    increment = block_size -1
    len_charac = len(charac)
    i = 0
    while i < len_charac:
        if (charac[i] == " ") and (i != increment):
            word_count = word_count + 1
            i = i + 1
        elif (charac[i] == " ") and (i == increment):

            word_count = word_count + 1
            increment = increment + block_size
            s.append(-1)
            i = i + 1
        elif (charac[i] != " ") and (i == increment):
            increment = increment + block_size + 1
            s.append(words[word_count])
            i = i + 1
        else:
            i = i + 1
    return s

def final_destination (words, block_size): # this is the function which use possible_syllables function gives the string with identation but no spacing.
    temp = ''
    len_of_temp = len(temp)
    output = []
    word_count = 0
    increment = block_size
    while word_count < len(words):
        if len_of_temp < increment:
            if len(words[word_count]) + len_of_temp < increment:
                temp = temp + words[word_count] + " "
                #print temp
                len_of_temp = len(temp)
                #print len_of_temp
                word_count = word_count + 1
            else:
                rem = increment - len_of_temp
                #print rem
                poss = possible_syllables(words[word_count])
                #print poss
                if poss == []:
                    temp = temp + "\n"
                    len_of_temp = len(temp) - 1
                    increment = increment + block_size
                elif '-' in poss[0]:
                    slc = poss[0].split('-')
                    #print slc
                    if len(slc[0]) <= rem:
                        temp = temp+slc[0] +"-\n"
                        len_of_temp = len(temp) - 1
                        #print temp
                        output.append(temp)
                        #print output
                        increment = increment + block_size
                        words[word_count] = slc[1]
                        #print words[word_count]
                    else:
                        temp = temp + "\n"
                        len_of_temp = len(temp) - 1
                        output.append(temp)
                        increment = increment + block_size
                else:
                    temp = temp + "\n"
                    len_of_temp = len(temp) - 1
                    output.append(temp)
                    increment = increment + block_size
        else:
            word_count = word_count + 1
    return temp

def possible_syllables(word): # this function simply returns all possible syllables of a particular word
    s = []
    if type(word) == int:
        return s
    word = word.lower()
    if len(word) < 4:
        s.append(word)
        return s
    temp = ""
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count = +1
        temp = word[0] + "-" + word[1:]
        s.append(temp)
    for index in range(1, len(word)):
        if word[index] in vowels and word[index-1] not in vowels:
            count += 1
            temp = word[0 : index+2] + "-" + word[index+2:]
            s.append(temp)
            if word.endswith("e"):
                count -= 1
                s.pop()
    if not s:
        s.append(word)
        return s
    if s[-1].endswith("-"):
        s.pop()
    return s


def sensitive_words(special): # this function returns the dictionaries of all possible syllables of those words which need to break into syllables.
    possbilities = {}
    for word in special:
        temp = possible_syllables(word)
        #print(temp)
        possbilities[word] = temp
    return possbilities

def manipulate_special(take_care_words, words):
    for word in words:
        if word in take_care_words:
            #print word
            #print take_care_words.get(word)[0]
            loc = words.index(word)
            words[loc] = take_care_words.get(word)[0]

def insert_enter_characters(modified_charac, block_size):
    count = 0
    changes = []
    increment = block_size -1
    last_space = -1
    i = 0
    increment = block_size -1
    for ch in modified_charac:
        if ch == " ":
            last_space = i
        if ch == "-":
            changes.append(i+1+count)
            count = count + 1
        i = i + 1
    for x in changes:
        modified_charac.insert(x, "\n")

'''

with open ('sample.txt') as f:
    char_per_line = f.readline().rstrip()  # this will just read the first line in a text file



try:
    char_per_line = int(char_per_line) # this will convert first line to integer
except:
    sys.stderr.write("first line cannot get converted into integer")
'''
input = ''
i = 1
char_per_line = ''
for line in sys.stdin:
    if i == 1:
        line = line.rstrip()
        char_per_line = char_per_line + line
    else:
        line = line.rstrip()
        input = input + line
    i = i + 1

print input

print char_per_line


try:
    char_per_line = int(char_per_line) # this will convert first line to integer
except:
    sys.stderr.write("first line cannot get converted into integer")

print type(char_per_line)

'''
with open('sample.txt') as f:
    next(f)
    for line in f:
        line = line.rstrip()
        input = input + line + " "
'''
input = input.rstrip()
input = input.replace("-","") # this will remove all existing hyphens from the text.
#print(input)
if len(input) < char_per_line:
    print("Error")
else:
    print("cool!")

words = input.split()

#print(words)
charac = (list) (input)

#print "charac ", len(charac)
#print "input ", len(input)

special = special_words(charac, words, char_per_line)
#print special
take_care_words = sensitive_words(special)
#print(take_care_words)

output = final_destination(words, char_per_line)

#print output
output = output.rstrip()
advanced_output = output.split("\n")
#print advanced_output

# this part of code even spacing between the strings
final_output =""
for line in advanced_output:
    if len(line) < char_per_line:
        rem = char_per_line - len(line)
        i = 0
        j = len(line)
        while i < j:
            if rem == 0:
                break
            if rem % 2 != 0:
                if line[i] == " ":
                    line = line[0:i] + " " + line[i:]
                    rem = rem -1
                i += 1
            else:
                if line[j-1] == " ":
                    line = line[0:j] + " " + line[j:]
                    rem = rem -1
                j -= 1
    #print line
    final_output = final_output + line + "\n"
#print "\n-------\n"
#print final_output # this is the final output.
sys.stdout.write(final_output)




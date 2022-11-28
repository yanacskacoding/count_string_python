'''
Write a program that asks a user to enter a string and print out the length, and duplicates it.

Note: Do not use String class' "len" method.

Example:
>>>
Enter a word: computer                                                                        
The length is 8. 
computercomputer
'''


#Code:
def remove_qoutes(thisString):
    return(thisString.replace("'", ""))

def remove_spaces(thisString):
    return(thisString.replace("", ""))

def wordLenth(word):
    return len(word)

word = input()
word = remove_qoutes(word)
word = remove_spaces(word)
word = str(word)


wordLenth = wordLenth(word)

print('The length is %i.' % (wordLenth))
print("%s%s" % (word,word))
s = "Taiwan is a country in East Asia, located at the junction of the East, and South China seas."

#break into list of words
word_list = s.split()

#print out the word list with a loop so that every 2 word is in full uppercase
counter = 1
for word in word_list:
    word = word.replace('.', '') # replace . with empty list
    word = word.replace(',', '') # replace , with empty list
    if counter.is_integer() == True:
        print(word.upper())
    else:
        print(word)
    counter = counter + 0.5

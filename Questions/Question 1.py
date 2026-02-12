file = open("../Provided Files/sample-file.txt", mode="r")

wordsList=[]

for line in file:
    lineSplitList = line.split()
    for word in lineSplitList:
        word = word.lower().strip(",.!?") # normalizes the word
        # bu putting it in lowercase and removing punctuation simultaneously
        
        if len(word) > 0: # checking if the word is not just whitespace
            wordsList.append(word)
file.close()

wordFrequencyDictionary = {}

# make a key-value pair for the word and its frequency
for word in wordsList:
    if word not in wordFrequencyDictionary:
        wordFrequencyDictionary[word] = 1
    else:
        wordFrequencyDictionary[word] += 1

sortedwordFrequencyDictionary = sorted(wordFrequencyDictionary.items(), key=lambda word: word[1], reverse=True)


# set variables to print the most frequent words,
# starting from #1 most frequent to #10 most frequent
i=0
if len(sortedwordFrequencyDictionary) < 10:
    maxFreq = len(sortedwordFrequencyDictionary)
else:
    maxFreq = 10
    
# print either all or the top 10 most frequent words
while i in range(0, maxFreq):
    print(sortedwordFrequencyDictionary[i][0],"->",sortedwordFrequencyDictionary[i][1], end="\n")
    i+=1

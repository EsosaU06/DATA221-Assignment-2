file = open("../Provided Files/sample-file.txt", mode="r")

wordsList=[]

for line in file:
    lineSplit = line.split()
    
    for word in lineSplit:
        word = word.lower().strip(",.!?")
        
        if len(word) > 1:
            wordsList.append(word)
    
file.close()

wordFreq = {}

# make a key-value pair for the word and its frequency
for word in wordsList:
    if word not in wordFreq:
        wordFreq[word] = 1
    else:
        wordFreq[word] += 1

sortedWordFreq = sorted(wordFreq.items(), key=lambda word: word[1], reverse=True)


# set variables to print the most frequent words,
# starting from #1 most frequent to #10 most frequent
i=0
if len(sortedWordFreq) < 10:
    maxFreq = len(sortedWordFreq)
else:
    maxFreq = 10
    
# print either all or the top 10 most frequent words
while i in range(0, maxFreq):
    print(sortedWordFreq[i][0],"->",sortedWordFreq[i][1], end="\n")
    i+=1

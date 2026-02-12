file = open("../Provided Files/sample-file.txt", mode="r")

wordsList=[]

for line in file:
    lineSplit = line.split()
    
    for word in lineSplit:
        word = word.lower()
        word = word.strip(",.!?")
        
        if len(word) > 1:
            wordsList.append(word)
file.close()

bigramList = []

# let i = the current index
for i in range(0, len(wordsList)-1): # avoid errors with bounds, the bigram goes from i to the next index
    bigramList.append((wordsList[i], wordsList[i+1]))
    
bigramFreq = {}
# essentially the same logic as the last question
for bigram in bigramList:
    if bigram not in bigramFreq:
        bigramFreq[bigram] = 1
    else:
        bigramFreq[bigram] += 1

if len(bigramFreq) < 5:
    maxFreq = len(bigramFreq)
else:
    maxFreq = 5

sortedBigramFreq = sorted(bigramFreq.items(), key=lambda bigram: bigram[1], reverse=True)
# sorting using a lambda function
# (source: https://www.geeksforgeeks.org/python/ways-sort-list-dictionaries-values-python-using-lambda-function/)

i=0 # iterate through the 3d list of frequencies
while i in range(0, maxFreq):
    print(sortedBigramFreq[i][0][0], sortedBigramFreq[i][0][1],"->",sortedBigramFreq[i][1], end="\n")
    i+=1


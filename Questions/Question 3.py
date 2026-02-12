import re

file = open("../Provided Files/sample-file.txt", mode="r")
fileLines = []

normalFile = [] # a file with the original punctuation
for fileLine in file:
    newFileLine = fileLine.replace(" ", "").lower()
    newFileLine = re.sub(r"[^\w\s]", "", newFileLine)
    
    if len(newFileLine) != 0 and newFileLine != "\n": # skips over empty lines
        fileLines.append(newFileLine)
        normalFile.append(fileLine)
file.close()

compareList = []
comparisonLineAndIndex = [] 

i=0
for i in range(0, len(fileLines)): #iterate through every line in fileLines and check if its already in the list
    if fileLines[i] in compareList:
        comparisonLineAndIndex.append([i, normalFile[i]]) # i found this easier than working with a dictionary
    else:
        compareList.append(fileLines[i])

print(f"There are {len(comparisonLineAndIndex)} near-duplicate sets.\n") # the amount of elements in the near-duplicate list
# indicate how many near-duplicates were found

print("First two sets of near-duplicates:")

print(comparisonLineAndIndex[0][0],": ", comparisonLineAndIndex[0][1])
print(comparisonLineAndIndex[1][0],": ", comparisonLineAndIndex[1][1])



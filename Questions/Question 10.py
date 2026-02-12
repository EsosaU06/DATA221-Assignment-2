def find_lines_containing(filename, keyword):
    lineAndIndex = []
    
    try:
        file = open(f"../Provided Files/{filename}", mode="r")
        currentLineIndex = 1
        
        for line in file:
            if keyword in line:
                lineAndIndex.append([currentLineIndex, line])
            currentLineIndex += 1
            # i find this way is easiest to save the index when reading from a file
        file.close()
        
    except FileNotFoundError:
        print("Error: the file cannot be found.")
        # error catching, in case the file was written wrong or does not exist
    
    else:
        print(f"{len(lineAndIndex)} lines containing the keyword ({keyword}) were found.\n")
        
        if len(lineAndIndex) < 3 and len(lineAndIndex) !=0 :
            amountInLines = len(lineAndIndex)
            print(f"The lines found are:\n")
            
        elif len(lineAndIndex) == 0:
            amountInLines = 0
            
        else:
            amountInLines = 3
            print(f"The first {amountInLines} found are:\n")
        
        lineCount=0
        for lineCount in range(0, amountInLines):
            print(f"Line {lineAndIndex[lineCount][0]}:")
            print(lineAndIndex[lineCount][1])

# uses the name and the extension
find_lines_containing("sample-file.txt", "lorem")

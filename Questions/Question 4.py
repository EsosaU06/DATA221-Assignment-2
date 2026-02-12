import pandas 

# create a pandas dataframe from the csv provided
studentDataFrame = pandas.read_csv("../Provided Files/student.csv")

# print(studentDataFrame)

# filter the dataset three times for the 3 conditions we need to filter
# three at a time so in order to be in the new dataset, you
# must fit the previous conditions
filterByStudyTime = studentDataFrame[studentDataFrame["studytime"] >= 3] 
filterbyInternet =  filterByStudyTime[filterByStudyTime["internet"] == 1]
studentDataFrameFullyFiltered = filterbyInternet[filterbyInternet["absences"] <= 5]

# write the resulting dataframe into a csv,
# assuming the index of each student is not needed
studentDataFrameFullyFiltered.to_csv("../Program-Created Files/high_engagement.csv", index=False)


# the amount of students would just be the rows, (each student has five
# "atributes", which are the columns)
# so find the amount of rows
rowsOfStudentDataFrameFullyFiltered = len(studentDataFrameFullyFiltered)
print("Amount of students:",rowsOfStudentDataFrameFullyFiltered)

# assuming median is the average used
medianOfStudentDataFrameFullyFiltered = studentDataFrameFullyFiltered["grade"].median()
print("Median grade:", medianOfStudentDataFrameFullyFiltered )



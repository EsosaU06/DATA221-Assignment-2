import pandas
import csv

studentDataFrame = pandas.read_csv("../Provided Files/student.csv")

i=1

# create new column from the conditions of a previous column
studentDataFrame.loc[studentDataFrame["grade"] <= 9, "grade_band"] = "Low"
studentDataFrame.loc[(studentDataFrame["grade"] >= 10) & (studentDataFrame["grade"] <=14), "grade_band"] = "Medium"
studentDataFrame.loc[studentDataFrame["grade"] > 14, "grade_band"] = "High"
# (source: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html)

# studentDataFrame["band"] = df["studentDataFrame"].map(gradeToBand)

# print(studentDataFrame)
bandColumnAmount = studentDataFrame["grade_band"].value_counts()
bandColumnCounts = [
    bandColumnAmount["Low"], bandColumnAmount["Medium"], bandColumnAmount["High"]  # create list of each value depending on its "key"
    ]

bandColumnAbsenceMean = studentDataFrame.groupby("grade_band")["absences"].mean().round(2) # round to improve readability

bandColumnAbsences = [
    bandColumnAbsenceMean["Low"], bandColumnAbsenceMean["Medium"], bandColumnAbsenceMean["High"]
    ]

bandColumnInternetAccess = (studentDataFrame.groupby("grade_band")["internet"].mean() * 100).round(2)
bandColumnInternet = [
    bandColumnInternetAccess["Low"], bandColumnInternetAccess["Medium"], bandColumnInternetAccess["High"]
    ]

# no print statements were specified, this just writes to the csv
with open("../Program-Created Files/student_bands.csv", "w", newline="") as csvfile: # write to the csv file
    studentBandsWriter = csv.writer(csvfile)
    studentBandsWriter.writerow(["Low", "Medium", "High"])
    studentBandsWriter.writerow(bandColumnCounts)
    studentBandsWriter.writerow(bandColumnAbsences)
    studentBandsWriter.writerow(bandColumnInternet)
    
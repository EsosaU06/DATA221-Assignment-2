import pandas

crimeDataFrame = pandas.read_csv("../Provided Files/crime.csv")

# create new column from the conditions of a previous columns
crimeDataFrame.loc[crimeDataFrame["ViolentCrimesPerPop"] >= 0.5, "risk"] = "High-Crime"
crimeDataFrame.loc[crimeDataFrame["ViolentCrimesPerPop"] < 0.5, "risk"] = "Low-Crime"
# (source: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html)

percentUnemployedByRisk = crimeDataFrame.groupby("risk")["PctUnemployed"].mean() # take the mean of the unemployed percentage
# grouped by the value of the risk column


print(f"Average unemployment rate for High-Crime group: {percentUnemployedByRisk['High-Crime'].round(2)}%")

print(f"Average unemployment rate for Low-Crime group: {percentUnemployedByRisk['Low-Crime'].round(2)}%")
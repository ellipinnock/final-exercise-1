# EXERCISE INSTRUCTIONS
# This script should output a list of column names from a CSV file with any spaces replaced by underscores (the '_' character)
# This script was started by someone else, and you've been asked to fix any errors and provide this functionality

import pandas
data = pandas.read_csv("weather_data/weather_year.csv")

col_names = data.columns.values.tolist()


# STEP 1 - Define a function below called "replace_whitespace" that can replace characters in a string with others. The function should take two parameters, the first being the string that needs whitespace characters replacing, and the second being the character to insert instead of the whitespace.

def replace_whitespace(inputString, characterToInsert):
	outputString=inputString.replace(' ', characterToInsert)
	return outputString

# STEP 2 - output the new column names generated by running your replace_whitespace function
# BONUS - trim any leading (at the front of the string) or trailing (at the end) whitespace characters from each column name before you call your replace_whitespace function

for i in range(len(col_names)):
	col_names[i]=replace_whitespace(col_names[i].lstrip().rstrip(), '_')

# STEP 3 - Using the shell:
# (a) write ONLY the new non-whitespace column names to a new file called columnNames instead of the shell output (stdout)

f1=open('columnNames.txt', 'a')
for i in col_names:
	f1.write(str(i) + '\n')
f1.close()

# (b) similarly, sort the outputted column names into a new file called sortedColumnNames

sorted_cols=sorted(col_names)

f2=open('sortedColumnNames.txt', 'a')
for i in sorted_cols:
	f2.write(str(i) + '\n')
f2.close()

# Push the following files to Aleksandra's github: this file containing the fixed code, file with the column names with spaces removed, and the file with the sorted names
# This will raise a pull request, so we can check your script

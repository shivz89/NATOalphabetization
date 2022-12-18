# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:

{"A": "Alfa", "B": "Bravo"}

import pandas

df = pandas.read_csv('workingCSV/NATO-alphabet-start/nato_phonetic_alphabet.csv')
alphabet_dict = {row.letter:row.code for (index,row) in df.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input ("Enter your name: ").upper()
name_list = [letter for letter in name]
nato_alphabets = []

for c in name_list:
    {nato_alphabets.append(value) for (key, value) in alphabet_dict.items() if c == key}

print(nato_alphabets)

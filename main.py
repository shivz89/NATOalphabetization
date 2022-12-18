import pandas

df = pandas.read_csv('workingCSV/NATO-alphabet-start/nato_phonetic_alphabet.csv')
alphabet_dict = {row.letter:row.code for (index,row) in df.iterrows()}


name = input ("Enter your name: ").upper()
name_list = [letter for letter in name]
nato_alphabets = []

for c in name_list:
    {nato_alphabets.append(value) for (key, value) in alphabet_dict.items() if c == key}

print(nato_alphabets)

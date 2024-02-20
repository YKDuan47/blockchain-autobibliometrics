import pandas as pd
import matplotlib.pyplot as plt
import metaknowledge as mk

RC = mk.RecordCollection('data')
selectedTags = ['J9', 'C1']
RC.writeCSV('topScientist.csv',onlyTheseTags=selectedTags)

df = pd.read_csv('topscientist.csv')
Journal = df['J9']
#print(Journal,type(Journal))

i = 0
txt = '|'
for scientist in  Journal:
    #AU_words = str(Journal[i]).split()
    #firstnameAuthor = AU_words[0]
    #lastnameAuthor = AU_words[:2]
    #Journal[i] = lastnameAuthor
    Journal[i] = str(Journal[i]).split(txt, 1)[0]
    #df['J9'] = Journal[i]
    i += 1

#print(Journal)
counts = pd.value_counts(Journal)
print(counts[:15])
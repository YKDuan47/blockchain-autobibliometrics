import pandas as pd
import matplotlib.pyplot as plt
import metaknowledge as mk

RC = mk.RecordCollection('data')
selectedTags = ['AF', 'C1','PY']
RC.writeCSV('topScientist.csv',onlyTheseTags=selectedTags)

df = pd.read_csv('topscientist.csv')
scientists = df['AF']
#print(scientists,type(scientists))

i = 0
txt = '|'
for scientist in  scientists:
    #AU_words = str(scientists[i]).split()
    #firstnameAuthor = AU_words[0]
    #lastnameAuthor = AU_words[:2]
    #scientists[i] = lastnameAuthor
    scientists[i] = str(scientists[i]).split(txt, 1)[0]
    #df['AU'] = scientists[i]
    i += 1

#print(scientists)
counts = pd.value_counts(scientists)
print(counts[:15])
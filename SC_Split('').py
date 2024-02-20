import pandas as pd

df = pd.read_csv('aaaaa.csv')
a = len(df)
for i in range(a):
    s = df.iloc[i,1]
    l = s.split("|")
    if len(l) > 1:
        df.iloc[i,1] = l[0]
        for item in range(len(l[1:])):
            new_row = df.iloc[i].copy()  # Copy the current row
            new_row[1] = l[1:][item]  # Replace the second column with the split data
            df = df.append(new_row, ignore_index=True)  # Append the new row to df
    if i % 500 == 0:
        print(f'Progress: {i/a*100:.2f}%')

df.to_csv('aaaaa_1.csv',index=False)
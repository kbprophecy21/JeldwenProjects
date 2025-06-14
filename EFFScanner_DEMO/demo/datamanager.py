import pandas as pd

PATH = './Data/sample.txt'

df = pd.read_csv(PATH)

for index, row in df.iterrows():
    print(row)
import pandas as pd
import os
import numpy as np
from pandas import ExcelWriter

path = '../result/'

# list all files in 'path' dir
files = os.listdir(path)

# just pick xlsx files
files_xls = [f for f in files if f[-4:] == 'xlsx']
print(files_xls)

# initial data frame
df = pd.DataFrame()


# loop through all files
for f in files_xls:

    # other excel file
    data = pd.read_excel(path + f)

    # append all data excel data frame
    df = df.append(data, ignore_index=True)


# data reorder (with nominal data top priority, numeric back)
nominal_title = ['Report Date', 'Customer','Type', 'Item Short Name', 'Brand', 'Sales']
reordered = nominal_title + [i for i in df.columns if i not in nominal_title]
df = df[reordered]

# change numeric data NaN to -1
df.iloc[:, 6:] = df.iloc[:, 6:].apply(pd.to_numeric, errors='coerce').fillna(-1)



# write to excel
writer = ExcelWriter('../result/final/WPG_data.xlsx')
df.to_excel(writer)
writer.save()

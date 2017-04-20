import pandas as pd
import os
import numpy as np
from pandas import ExcelWriter

path = '../data/86122/'

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
    data = pd.read_excel('../data/86122/'+ f, skiprows=2)
    excel_date = pd.read_excel('../data/86122/'+ f, skip_footer=len(data.index)+1)
    if excel_date.iloc[0][1] == 'Report Date：' :
        data.insert(0, 'Report Date', excel_date.iloc[0][2])
        print( excel_date.iloc[0][2])

    else:
        data.insert(0, 'Report Date', excel_date.iloc[0][1])
        print( excel_date.iloc[0][1])

    # append all data excel data frame
    df = df.append(data, ignore_index=True)



# print(df)


# data reorder (with nominal data top priority, numeric back)
nominal_title = ['Report Date', 'Customer','Type', 'Item Short Name', 'Brand', 'Sales']
reordered = nominal_title + [i for i in df.columns if i not in nominal_title]
df = df[reordered]

# change numeric data NaN to -1
df.iloc[:, 6:] = df.iloc[:, 6:].apply(pd.to_numeric, errors='coerce').fillna(-1)



# write to excel
writer = ExcelWriter('../result/86122.xlsx')
df.to_excel(writer)
writer.save()




# get excel title
# title = list(df)

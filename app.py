import numpy as np
import pandas as pd
from pandas import ExcelWriter
import openpyxl
import datetime
from clustering.som import SOM
from model import reformat


#-----------------------------------Data pre-process-------------------------------------------------------
# get  training data
df = pd.read_excel('./data/WPG_data_test.xlsx')

# define which title to be noimal
df_nominal = df.ix[:, ['Report Date', 'Customer', 'Type','Item Short Name', 'Brand', 'Sales']]
df_numerical_tmp = df.ix[:, ['OH WK', 'OH FCST WK', 'BL WK', 'BL FCST WK', 'Last BL', 'Backlog', 'BL <= 9WKs', 'DC OH', 'On the way', 'Hub OH', 'Others OH', 'Avail.', 'Actual WK', 'FCST WK', 'Actual AWU', 'FCST AWU', 'FCST M', 'FCST M1', 'FCST M2', 'FCST M3']]
df_numerical = df_numerical_tmp.apply(pd.to_numeric, errors='coerce').fillna(0)

# concat nominal title to _201_107_Zer_T6W_TOS_Joe format
# title_concat( @param1(df): nominal_dataframe,
#               @param2(int): first N char )
# label_abbr = reformat.title_concat(df_nominal,3);

# force str to numeric datatype (if not => NaN) then replace NaN to 0


# get data dim to latter SOM prcess
input_dim = len(df_numerical.columns)

# change data to np array (SOM accept nparray format)
input_data = np.array(df_numerical)



#-----------------------------------SOM process-------------------------------------------------------

#Train a 20x30 SOM with 400 iterations
som = SOM(7, 7, input_dim, 50)
print('training start : ' + str(datetime.datetime.now()))
som.train(input_data)


#Get output grid for visualization
image_grid = som.get_centroids()


#Map datato their closest neurons
mapped = som.map_vects(input_data)
result = np.array(mapped)


#-------------------------------------Output format-----------------------------------------------------

# output format
output_np = np.concatenate((df_nominal, result), axis=1)
output_pd = pd.DataFrame(data=output_np, columns=['Report Date', 'Customer', 'Type', 'Item Short Name', 'Brand', 'Sales', 'axis-x', 'axis-y'])
# print(output_pd)


# write to final csv
output_pd.to_csv('./result/result.csv')

import numpy as np
import pandas as pd

df = pd.read_excel('./data/WPG_data_test.xlsx')

# -----------------------------------input data random pre-process------------------------------------
df_ran = df.sample(frac=1)

# define which title to be noimal
# df_nominal = df_ran.ix[:, ['Report Date', 'Customer', 'Type','Item Short Name', 'Brand', 'Sales']]
df_nominal = df_ran.ix[:, ['Sales']]
df_numerical_tmp = df_ran.iloc[:,6:]
df_numerical = df_numerical_tmp.apply(pd.to_numeric, errors='coerce').fillna(-1)
df_numerical['ZeroSeparater'] = 0

result = pd.concat([df_numerical, df_nominal], axis=1)

df_final = df_ran.ix[:, ['ZeroSeparater', 'Sales']]
df_final.ix[:, ['ZeroSeparater']]= df_final.ix[:, ['ZeroSeparater']].fillna(0).astype(int)


np.savetxt(r'./scalaResult/wpg_test_sales.txt', df_final.values, fmt='%s')

# ----------------------------------------------below prepare numerical data-----------------
# df_nominal = df_ran.ix[:, ['Sales']]
# df_numerical_tmp = df_ran.iloc[:,6:]
# df_numerical = df_numerical_tmp.apply(pd.to_numeric, errors='coerce').fillna(-1)
#
# result = pd.concat([df_numerical, df_nominal], axis=1)
#
# np.savetxt(r'./scalaResult/wpg_test_sales.txt', result.values, fmt='%s')
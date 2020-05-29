# Machine Learning SOM assignemnt - (2017/4/19)
------
## Description
* #### Folder structure

```
.
│   README.md
│   app.py   
│
└───clustering
│   │   __init__.py
│   │   som.py
│   
└───data
│   │   WPG_data.xlsx
│   │   WPG_data_test.xlsx
│   └───1171
│       │   DDRStockReport_AITG_1171 (1).xlsx
│       │   DDRStockReport_AITG_1171 (2).xlsx
│       │   ...
│   
└───model
│   │   joinexcel_final.py
│   │   joinexcel.py
│   │   reformat.py
│   
└───result
    │   result.csv

```

* #### 使用到的python package
    下載完後須確認本幾環境安裝此 packages
    * Python 3.5.*

    > python 2.* 需要 xlrd package

    * tensorflow !!!
    * pandas
    * openpyxl
    * numpy

* #### Main file description

    1. #### app.py

    program endpoint，include read data、execute SOM、output to `.csv` file。

    change `df_nominal` to `['Report Date', 'Customer', 'Type','Item Short Name', 'Brand', 'Sales']` and select nominal label_abbr

    更改 `df_numerical_tmp` 變數中的 ` ['OH WK', 'OH FCST WK', 'BL WK',........]` 選取需要丟進去 SOM 跑的 input Data.

    更改 `som = SOM(7, 7, input_dim, 50)` 其中的 7 * 7為輸出的loaction map 長相, 50為跑的迴圈數量

    2.  #### clustering > som.py

    SOM 演算法實作檔案，如果需要更改 neighborhood function 等演算法更改，須更改此檔案。

    3. #### data

    所有資料皆存再此檔案中。`WPG_data.xlsx` 為整理好的總表，此次可以使用此表做操作。

    > `WPG_data_test.xlsx` 是為 `WPG_data.xlsx` 的前面50比資料。（debug用，要麼 SOM 跑太久了）

    3. #### result

    跑完結果儲存的地方，結果麻煩請參考我的範例 `result.csv` 喔！感激不盡～

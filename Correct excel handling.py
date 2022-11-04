Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> file = pd.ExcelFile("C:\Users\Vurgune Bagirova\Desktop\original.xlsx")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> import pandas as pd
>>> file = pd.ExcelFile("C:/Users/Vurgune Bagirova/Desktop/original.xlsx")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    file = pd.ExcelFile("C:/Users/Vurgune Bagirova/Desktop/original.xlsx")
  File "C:\Python38\lib\site-packages\pandas\io\excel\_base.py", line 824, in __init__
    self._reader = self._engines[engine](self._io)
  File "C:\Python38\lib\site-packages\pandas\io\excel\_xlrd.py", line 21, in __init__
    super().__init__(filepath_or_buffer)
  File "C:\Python38\lib\site-packages\pandas\io\excel\_base.py", line 353, in __init__
    self.book = self.load_workbook(filepath_or_buffer)
  File "C:\Python38\lib\site-packages\pandas\io\excel\_xlrd.py", line 36, in load_workbook
    return open_workbook(filepath_or_buffer)
  File "C:\Python38\lib\site-packages\xlrd\__init__.py", line 111, in open_workbook
    with open(filename, "rb") as f:
FileNotFoundError: [Errno 2] No such file or directory: 'C:/Users/Vurgune Bagirova/Desktop/original.xlsx'
>>> import pandas as pd
>>> file = pd.ExcelFile("C:/Users/Vurgune Bagirova/Downloads/original.xlsx")
>>> print(file.sheet_names)
['sales', 'customers']
>>> sheet1 = file.parse('sales')
>>> print(sheet1)
        Date             Customer  Invoice  Amount
0 2018-12-01  Steel Brothers Inc.       98    1340
1 2018-12-10             MMC Inc.       99    1900
2 2018-12-12             MMC Inc.      100    2900
3 2018-12-18  Steel Brothers Inc.      101     977
4 2018-12-21     Steel & Iron LLC      102    3400
>>> type(sheet1)
<class 'pandas.core.frame.DataFrame'>
>>> print(sheet1.Date)
0   2018-12-01
1   2018-12-10
2   2018-12-12
3   2018-12-18
4   2018-12-21
Name: Date, dtype: datetime64[ns]
>>> sheet1.Amount
0    1340
1    1900
2    2900
3     977
4    3400
Name: Amount, dtype: int64
>>> sheet1.Amount.sum()
10517
>>> sheet1.loc[0]
Date        2018-12-01 00:00:00
Customer    Steel Brothers Inc.
Invoice                      98
Amount                     1340
Name: 0, dtype: object
>>> sheet1.loc[0, "Amount"]
1340
>>> sheet1.set_index("Customer", inplace = True)
>>> sheet1.loc["MMC Inc."]
               Date  Invoice  Amount
Customer                            
MMC Inc. 2018-12-10       99    1900
MMC Inc. 2018-12-12      100    2900
>>> sheet1 = sheet1.reset_index()
>>> sheet1["Invoice"]
0     98
1     99
2    100
3    101
4    102
Name: Invoice, dtype: int64
>>> type(sheet1["Invoice"])
<class 'pandas.core.series.Series'>
>>> sheet1.loc[sheet1.["Invoice"] == 99]
SyntaxError: invalid syntax
>>> sheet1.loc[sheet1["Invoice"] == 99]
   Customer       Date  Invoice  Amount
1  MMC Inc. 2018-12-10       99    1900
>>> sheet1.loc[sheet1["Amount"] > 2000]
           Customer       Date  Invoice  Amount
2          MMC Inc. 2018-12-12      100    2900
4  Steel & Iron LLC 2018-12-21      102    3400
>>> sheet1.loc[sheet1["Amount"].idxmax()]
Customer       Steel & Iron LLC
Date        2018-12-21 00:00:00
Invoice                     102
Amount                     3400
Name: 4, dtype: object
>>> sheet1.loc[sheet1["Amount"].idxmax()]["Customer"]
'Steel & Iron LLC'
>>> sheet1.loc[sheet1["Amount"]>1800]
           Customer       Date  Invoice  Amount
1          MMC Inc. 2018-12-10       99    1900
2          MMC Inc. 2018-12-12      100    2900
4  Steel & Iron LLC 2018-12-21      102    3400
>>> sheet1.loc[sheet["Amount"] > 1800]["Customer"]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    sheet1.loc[sheet["Amount"] > 1800]["Customer"]
NameError: name 'sheet' is not defined
>>> sheet1.loc[sheet1["Amount"] > 1800 ]["Customer"]
1            MMC Inc.
2            MMC Inc.
4    Steel & Iron LLC
Name: Customer, dtype: object
>>> sheet1.loc[sheet1["Amount"]>1800]["Customer"].unique()
array(['MMC Inc.', 'Steel & Iron LLC'], dtype=object)
>>> sheet1.loc[sheet1["Amount"]>1800]["Customer"].unique()[0]
'MMC Inc.'
>>> for customer in sheet1.loc[sheet1["Amount"] > 1800]["Customer"].unique():
	print(customer)

	
MMC Inc.
Steel & Iron LLC
>>> 
Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> file = pd.ExcelFile("C:\Users\Vurgune Bagirova\Downloads\original.xlsx")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> import pandas as pd
>>> file = pd.ExcelFile("\Users\Vurgune Bagirova\Downloads\original.xlsx ")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 0-1: truncated \UXXXXXXXX escape
>>> import pandas as pd
>>> file = pd.ExcelFile("/Users/Vurgune Bagirova/Downloads/original.xlsx")
>>> print(file.sheet_names)
['sales', 'customers']
>>> sheet = file.parse('customers')
>>> print(sheet)
              Customer                     Address  ...          Phone       Contact
0  Steel Brothers Inc.      33 David Avenue, Paris  ...  +33 262515162    Anne Smith
1             MMC Inc.  22 Marcus St, Orrville, OH  ...   +1 272625623    John Green
2     Steel & Iron LLC     Rua do Raio, 566. Braga  ...  +351 27626526  Carlos Gomes

[3 rows x 5 columns]
>>> type(sheet)
<class 'pandas.core.frame.DataFrame'>
>>> print(sheet.Date)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(sheet.Date)
  File "C:\Python38\lib\site-packages\pandas\core\generic.py", line 5274, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'Date'
>>> print(sheet.Date)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(sheet.Date)
  File "C:\Python38\lib\site-packages\pandas\core\generic.py", line 5274, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'Date'
>>> print(sheet['Date'])
Traceback (most recent call last):
  File "C:\Python38\lib\site-packages\pandas\core\indexes\base.py", line 2646, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 111, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 138, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1619, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1627, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Date'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(sheet['Date'])
  File "C:\Python38\lib\site-packages\pandas\core\frame.py", line 2800, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Python38\lib\site-packages\pandas\core\indexes\base.py", line 2648, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 111, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 138, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1619, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1627, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Date'
>>> print(sheet'[Date]')
SyntaxError: invalid syntax
>>> print(sheet[['Date']])
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(sheet[['Date']])
  File "C:\Python38\lib\site-packages\pandas\core\frame.py", line 2806, in __getitem__
    indexer = self.loc._get_listlike_indexer(key, axis=1, raise_missing=True)[1]
  File "C:\Python38\lib\site-packages\pandas\core\indexing.py", line 1552, in _get_listlike_indexer
    self._validate_read_indexer(
  File "C:\Python38\lib\site-packages\pandas\core\indexing.py", line 1640, in _validate_read_indexer
    raise KeyError(f"None of [{key}] are in the [{axis_name}]")
KeyError: "None of [Index(['Date'], dtype='object')] are in the [columns]"
>>> print(sheet(sales.Date))
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(sheet(sales.Date))
NameError: name 'sales' is not defined
>>> print(sales.Date)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(sales.Date)
NameError: name 'sales' is not defined
>>> print(sheet(sales'[Date]'))
SyntaxError: invalid syntax
>>> print(sheet(sales[Date]))
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    print(sheet(sales[Date]))
NameError: name 'sales' is not defined
>>> sheet1=file.parse('sales')
>>> print(sheet1.Date)
0   2018-12-01
1   2018-12-10
2   2018-12-12
3   2018-12-18
4   2018-12-21
Name: Date, dtype: datetime64[ns]
>>> sheet.Amount.sum()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    sheet.Amount.sum()
  File "C:\Python38\lib\site-packages\pandas\core\generic.py", line 5274, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'Amount'
>>> print(sheet1.Amount.sum())
10517
>>> print(sheet1.loc[1])
Date        2018-12-10 00:00:00
Customer               MMC Inc.
Invoice                      99
Amount                     1900
Name: 1, dtype: object
>>> print(sheet1.loc[0])
Date        2018-12-01 00:00:00
Customer    Steel Brothers Inc.
Invoice                      98
Amount                     1340
Name: 0, dtype: object
>>> print(sheet1."Amount")
SyntaxError: invalid syntax
>>> print(sheet1.loc[0, "Amount"])
1340
>>> print(sheet1.set_index("Customer", inplace=True)
      print(sheet1.loc["MMC Inc. "])
      
SyntaxError: invalid syntax
>>> print(sheet1.set_index("Customer", inplace = True)
       print(sheet1.loc["MMC Inc."])
      
SyntaxError: invalid syntax
>>> print(sheet1.set_index("Customer", inplace = True)
       sheet1.loc["MMC Inc."]
      
SyntaxError: invalid syntax
>>> print(sheet1.set_index("Customer", inplace = True)
       sheet1.loc[['MMC Inc.']]
      
SyntaxError: invalid syntax
>>> sheet1.set_index("Customer", inplace = True)
>>> sheet1.loc["MMC Inc."]
               Date  Invoice  Amount
Customer                            
MMC Inc. 2018-12-10       99    1900
MMC Inc. 2018-12-12      100    2900
>>> sheet = sheet1.reset_index()
>>> sheet1["Invoice"]
Customer
Steel Brothers Inc.     98
MMC Inc.                99
MMC Inc.               100
Steel Brothers Inc.    101
Steel & Iron LLC       102
Name: Invoice, dtype: int64
>>> type(sheet1["Invoice"])
<class 'pandas.core.series.Series'>
>>> sheet1.loc[ sheet1["Invoice"]] == 99]
SyntaxError: unmatched ']'
>>> sheet1.loc[ sheet1["Invoice"]] == 99
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    sheet1.loc[ sheet1["Invoice"]] == 99
  File "C:\Python38\lib\site-packages\pandas\core\indexing.py", line 1768, in __getitem__
    return self._getitem_axis(maybe_callable, axis=axis)
  File "C:\Python38\lib\site-packages\pandas\core\indexing.py", line 1954, in _getitem_axis
    return self._getitem_iterable(key, axis=axis)
  File "C:\Python38\lib\site-packages\pandas\core\indexing.py", line 1595, in _getitem_iterable
    keyarr, indexer = self._get_listlike_indexer(key, axis, raise_missing=False)
  File "C:\Python38\lib\site-packages\pandas\core\indexing.py", line 1552, in _get_listlike_indexer
    self._validate_read_indexer(
  File "C:\Python38\lib\site-packages\pandas\core\indexing.py", line 1640, in _validate_read_indexer
    raise KeyError(f"None of [{key}] are in the [{axis_name}]")
KeyError: "None of [Int64Index([98, 99, 100, 101, 102], dtype='int64', name='Customer')] are in the [index]"
>>> sheet1.loc[ sheet1["Invoice"] == 99 ]
               Date  Invoice  Amount
Customer                            
MMC Inc. 2018-12-10       99    1900
>>> sheet1.loc[ sheet1["Amount"] > 2000]
                       Date  Invoice  Amount
Customer                                    
MMC Inc.         2018-12-12      100    2900
Steel & Iron LLC 2018-12-21      102    3400
>>> sheet1.loc[ sheet1["Amount"].idxmax()]
Date       2018-12-21 00:00:00
Invoice                    102
Amount                    3400
Name: Steel & Iron LLC, dtype: object
>>> sheet1.loc[ sheet1["Amount"].idxmax()]["Customer"]
Traceback (most recent call last):
  File "C:\Python38\lib\site-packages\pandas\core\indexes\base.py", line 4410, in get_value
    return libindex.get_value_at(s, key)
  File "pandas\_libs\index.pyx", line 44, in pandas._libs.index.get_value_at
  File "pandas\_libs\index.pyx", line 45, in pandas._libs.index.get_value_at
  File "pandas\_libs\util.pxd", line 98, in pandas._libs.util.get_value_at
  File "pandas\_libs\util.pxd", line 83, in pandas._libs.util.validate_indexer
TypeError: 'str' object cannot be interpreted as an integer

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    sheet1.loc[ sheet1["Amount"].idxmax()]["Customer"]
  File "C:\Python38\lib\site-packages\pandas\core\series.py", line 871, in __getitem__
    result = self.index.get_value(self, key)
  File "C:\Python38\lib\site-packages\pandas\core\indexes\base.py", line 4418, in get_value
    raise e1
  File "C:\Python38\lib\site-packages\pandas\core\indexes\base.py", line 4404, in get_value
    return self._engine.get_value(s, k, tz=getattr(series.dtype, "tz", None))
  File "pandas\_libs\index.pyx", line 80, in pandas._libs.index.IndexEngine.get_value
  File "pandas\_libs\index.pyx", line 90, in pandas._libs.index.IndexEngine.get_value
  File "pandas\_libs\index.pyx", line 138, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1619, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1627, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Customer'
>>> sheet1.loc[ sheet1["Amount"].idxmax() ][ sheet1["Customer"]]
Traceback (most recent call last):
  File "C:\Python38\lib\site-packages\pandas\core\indexes\base.py", line 2646, in get_loc
    return self._engine.get_loc(key)
  File "pandas\_libs\index.pyx", line 111, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 138, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1619, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1627, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Customer'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    sheet1.loc[ sheet1["Amount"].idxmax() ][ sheet1["Customer"]]
  File "C:\Python38\lib\site-packages\pandas\core\frame.py", line 2800, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Python38\lib\site-packages\pandas\core\indexes\base.py", line 2648, in get_loc
    return self._engine.get_loc(self._maybe_cast_indexer(key))
  File "pandas\_libs\index.pyx", line 111, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 138, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 1619, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 1627, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Customer'
>>> sheet1.set_index("Customer", inplace = True)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    sheet1.set_index("Customer", inplace = True)
  File "C:\Python38\lib\site-packages\pandas\core\frame.py", line 4303, in set_index
    raise KeyError(f"None of {missing} are in the columns")
KeyError: "None of ['Customer'] are in the columns"
>>> sheet1.loc[0]
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    sheet1.loc[0]
  File "C:\Python38\lib\site-packages\pandas\core\indexing.py", line 1768, in __getitem__
    return self._getitem_axis(maybe_callable, axis=axis)
  File "C:\Python38\lib\site-packages\pandas\core\indexing.py", line 1964, in _getitem_axis
    self._validate_key(key, axis)
  File "C:\Python38\lib\site-packages\pandas\core\indexing.py", line 1831, in _validate_key
    self._convert_scalar_indexer(key, axis)
  File "C:\Python38\lib\site-packages\pandas\core\indexing.py", line 741, in _convert_scalar_indexer
    return ax._convert_scalar_indexer(key, kind=self.name)
  File "C:\Python38\lib\site-packages\pandas\core\indexes\base.py", line 2887, in _convert_scalar_indexer
    self._invalid_indexer("label", key)
  File "C:\Python38\lib\site-packages\pandas\core\indexes\base.py", line 3075, in _invalid_indexer
    raise TypeError(
TypeError: cannot do label indexing on <class 'pandas.core.indexes.base.Index'> with these indexers [0] of <class 'int'>
>>> print(sheet1.loc[0])
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    print(sheet1.loc[0])
  File "C:\Python38\lib\site-packages\pandas\core\indexing.py", line 1768, in __getitem__
    return self._getitem_axis(maybe_callable, axis=axis)
  File "C:\Python38\lib\site-packages\pandas\core\indexing.py", line 1964, in _getitem_axis
    self._validate_key(key, axis)
  File "C:\Python38\lib\site-packages\pandas\core\indexing.py", line 1831, in _validate_key
    self._convert_scalar_indexer(key, axis)
  File "C:\Python38\lib\site-packages\pandas\core\indexing.py", line 741, in _convert_scalar_indexer
    return ax._convert_scalar_indexer(key, kind=self.name)
  File "C:\Python38\lib\site-packages\pandas\core\indexes\base.py", line 2887, in _convert_scalar_indexer
    self._invalid_indexer("label", key)
  File "C:\Python38\lib\site-packages\pandas\core\indexes\base.py", line 3075, in _invalid_indexer
    raise TypeError(
TypeError: cannot do label indexing on <class 'pandas.core.indexes.base.Index'> with these indexers [0] of <class 'int'>
>>> 
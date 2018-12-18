import pandas as pd
from pandas import Series, DataFrame

con = pd.read_excel("2.xls", sheet_name="Sheet1")

result = [ str(i) + "0" * (12-len(str(i))) for i in con["first"]]
con["first"] = np.array(result)
DataFrame(con).to_excel('con.xlsx', sheet_name='Sheet1', index=False, header=True)
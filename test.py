import pandas as pd
import numpy as np


def diff_pd(df1, df2):
    """Identify differences between two pandas DataFrames"""
    assert (df1.columns == df2.columns).all(), \
        "DataFrame column names are different"
    if any(df1.dtypes != df2.dtypes):
        "Data Types are different, trying to convert"
        df2 = df2.astype(df1.dtypes)
    if df1.equals(df2):
        return None
    else:
        # need to account for np.nan != np.nan returning True
        diff_mask = (df1 != df2) & ~(df1.isnull() & df2.isnull())
        ne_stacked = diff_mask.stack()
        changed = ne_stacked[ne_stacked]
        changed.index.names = ['id', 'col']
        difference_locations = np.where(diff_mask)
        changed_from = df1.values[difference_locations]
        changed_to = df2.values[difference_locations]
        return pd.DataFrame({'from': changed_from, 'to': changed_to},
                            index=changed.index)
import sys
from io import StringIO

DF1 = StringIO("""id   Name   score                    isEnrolled           Comment
111  Jack   2.17                     True                 "He was late to class"
112  Nick   1.11                     False                "Graduated"
113  Zoe    NaN                     True                  " "
""")
DF2 = StringIO("""id   Name   score                    isEnrolled           Comment
111  Jack   2.17                     True                 "He was late to class"
112  Nick   1.21                     False                "Graduated"
113  Zoe    NaN                     False                "On vacation" """)
df1 = pd.read_table(DF1, sep='\s+', index_col='id')
df2 = pd.read_table(DF2, sep='\s+', index_col='id')
print(diff_pd(df1, df2))
#diff_pd(df1, df2).to_excel('orders2.xlsx', index=True)
writer = pd.ExcelWriter('diff.xlsx', engine='xlsxwriter')
diff_pd(df1, df2).to_excel(writer, sheet_name='Sheet1')
writer.save()
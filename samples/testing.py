import sys
import os

sys.path.append(os.getcwd() + '/correlation')

import numpy as np
import pandas as pd

try: 
    import correlation as co
    print("Successful import!")
    #import correlation.io.converter as converter

except:
    sys.exit("Can't find correlation")


file1 = str(sys.argv[1])
file2 = str(sys.argv[2])

print("file1: ", file1)
print("file2: ", file2)

ct1 = co.Container(filename=file1)
ct2 = co.Container(filename=file2)#, keep_cols=[1])

#if (file1.endswith("csv")):

#    ct1.df = co.convert(file1) #pd.read_csv(file1)

#if (file2.endswith("csv")):

#    ct2.df = co.convert(file2)

#print(ct1.df)
#print(ct2.df)

#print(ct1.return_col(col_num=1))
#print(ct1.return_col(col_name="births"))

print("ct1: ", ct1)
print("ct2: ", ct2)

#print(ct1.df[ct1.labels[1]])

print("Value range: ", ct1.get_range("births"))

ct1.resolve_dates(combine={"year":"year", "month":"month", "day":"date_of_month"})

print("new ct1: ", ct1)

ct1.add_each_year(date_col="ISO date", col_name="births")
zero=True
ct1.normalize_column(col_name="births", zero=zero)

print("bucket ct1: ", ct1.df)

ct1.overlap(ct2, match_cols=("year","year"))

print("changed ct1? : \n", ct1.df, '\n', ct2.df)

combinedct = ct1.combine(ct2, x1="year", x2="year", y1="births", y2="data")

print("Combined: \n", combinedct)


print("\n===Test complete===\n")

















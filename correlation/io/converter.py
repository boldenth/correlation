"""

calls parse_* based on input type
converts it to np.array or whatever is needed

"""

#import sys

#sys.path.append('/Users/Thomas/Documents/College/Career/\
#Projects/Correlation-Finder/correlation/correlation')

import numpy as np
import pandas as pd
import datetime as dt



def guess_extension(filename):

    extension = ".csv"

    return ".csv" # prevents infinite loops, and guesses csv if nothing else
                  # could create a new file with extension and open that
                  # since it does say convert

def convert_file(filename):

    if filename.endswith(".csv"):

        return pd.read_csv(filename)

    elif filename.endswith(".xlsx"):

        return pd.read_excel(filename)

    elif filename.endswith((".hdf5",".hdf",".h5")):

        return pd.read_hdf(filename)

    # for Google Sheets?
    # https://stackoverflow.com/questions/19611729/getting-
    # google-spreadsheet-csv-into-a-pandas-dataframe
    #elif filename.

    else: # as written this won't actually work because
          # there are extra chars at end of filename
          # and *that* file doesn't actually exist 

        ext = guess_extension(filename)
        try:
            convert_file(filename+ext)
        except:
            pd.read_table(filename)

def convert_time(time, dateonly=True):
    ''' assumes a string, returns ISO8601 string '''

    # YYYY-MM-DD HH:MM:SS (dateonly=False) <-- NOT implemented
    
    r_str = ""
    
    # YYYY-MM-DD
    if time.find('-') != -1:
        
        r_str = str(dt.datetime.strptime(time, '%Y-%m-%d'))\
                    .replace(' ', 'T') \
                    .replace(':','')   \
                    .replace('-','')
    
    # MM/DD/YYYY
    elif time.find('/') != -1:
        
        r_str = str(dt.datetime.strptime(time, '%m/%d/%Y'))\
                    .replace(' ', 'T') \
                    .replace(':','')   \
                    .replace('-','')
    
    # DD Month YYYY *or* DD Mon YYYY 
    else:
        
        abbr_to_num = {name.lower(): num for num, name \
                      in enumerate(cal.month_abbr) if num}

        name_to_num = {name.lower(): num for num, name \
                      in enumerate(cal.month_name) if num}
        
        try:
            
            three = time.split()
            
            try:
                
                three = [int(three[0]), 
                         abbr_to_num[three[1].lower()], 
                         int(three[2])]
                         
            except:
                three = [three[0], name_to_num[three[1].lower()], three[2]]
            
            r_str = str(dt.datetime(year=three[2],
                                    month=three[1],
                                    day=three[0]))\
                    .replace(' ', 'T') \
                    .replace(':','')   \
                    .replace('-','')
            
        except:
            print("Fail")
            r_str = time
    
    return r_str

if __name__ == "__main__": # for testing purposes mainly

    # get file extenstion to guess 

    file1 = str(sys.argv[1])
    file2 = str(sys.argv[2])

    print("file1: ", file1)
    print("file2: ", file2)

    if (file1.endswith("csv")):

        ct1.df = parse_csv(file1)

    if (file2.endswith("csv")):

        ct2.df = parse_csv(file2)

    #print(ct1.df)
    #print(ct2.df)

    print(ct1.return_col(col_num=1))
    print(ct2.return_col(col_name="here"))



#####
#
#  be able to reconcile the csvs using an input column for x and y axes
#  (either col number or col name) and keep only overlapping data.
#  this should be the only thing user has to interact with
#
#####
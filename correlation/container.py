#=============================================================================#
#
# container that is basically a pandas DataFrame object with more functionality
#
#=============================================================================#

# correlation functions
from .io.converter import convert_file, convert_time

import numpy  as np 
import pandas as pd
import datetime as dt
import calendar as cal

class Container(object):
    '''
    
    Parameters:
        string  filename   name of the file containing the data to be read
        list    keep_cols  column names or numbers of data to keep
        list    keep_rows  rows to keep, either numbers or range or
                           value range

    Attributes:
        DataFrame  df      Pandas DataFrame object
        dict       labels  names and indexes of each column in df
        int        size    number of rows in df

    Methods:
        add_each_year            .
        get_range                . 
        combine                  .
        keep_only_relevant_data  .
        normalize_column         .
        overlap                  .
        reshape                  .
        resolve_dates            .
        return_col               .
        set_dataframe            .
        shorten                  .
    
    '''

    def __init__(self, filename=None, keep_cols=None, keep_rows=None):

        self.df     = pd.DataFrame() # pandas' main data structure
        self.size   = 0              # number of rows
        self.labels = {} # dict (or list?) of each column num:label {1:"time"}
        self.active = (None, None)   # string tuple of active column names

        if filename is not None and isinstance(filename, str):
            print("File <" +filename+ "> given")
            self.set_dataframe(filename)

        if keep_cols is not None:
            #print("keeping cols") ### TODO: test, REMOVE
            self.keep_only_relevant_data(keep_cols)


    def reshape(self):

        listed = list(self.df)
        self.labels = {}

        for name in listed:
            self.labels[listed.index(name)] = name

        self.size = self.df.shape[0]


    def set_dataframe(self, filename):
        ''' 
        non-empty initialization from file passed 
        '''

        self.df = convert_file(filename)
        self.reshape()


    def get_range(self, column=""):
        ''' 
        returns max and min values in specified column name
        '''

        values = np.array([value for value in self.df[column]])

        return (values.min(), values.max())


    def set_active(self, col_names=None):
        '''
        col_names is a 2-tuple of column names to do analysis on
        '''

        if col_names is not None and isinstance(col_names, tuple):

            self.active = col_names


    def return_col(self, col_num=None, col_name=None):
        ''' 
        returns data in specified column as a Pandas Series 
        0-based indexing
        '''

        if col_name is not None and isinstance(col_name, str):
            return self.df[col_name]

        elif col_num is not None and isinstance(col_num, int):
            return self.df[self.labels[col_num]]

        else:
            return pd.Series()


    def keep_only_relevant_data(self, columns=[]):
        ''' 
        keeps data from column labels passed 
        '''

        temp_df = pd.DataFrame()

        for col in columns:

            if type(col) == int:
                temp_df[self.labels[col]] = self.df[self.labels[col]] 

            elif type(col) == str:
                temp_df[col] = self.df[col]

            else:
                raise SystemExit("Invalid keep_cols")

        self.df = temp_df
        self.reshape()


    def resolve_dates(self, cols=None, combine=None, dateonly=True): 
        ''' 
        converts dates to common ISO 8601 format in given columns 
        ISO 8601 format is: yyyymmddThhmmss

        can also combine date columns into one

        combine is a dictionary with keys "year", "month", "day"
        and values of actual column names

        cols is a list of column names with values that will be
        converted into ISO format date strings
        '''
       
        if combine is not None and isinstance(combine, dict):

            if dateonly: 

                iso_col = []

                for i, val in self.df.iterrows():

                    # in case the month is not an integer, make it one
                    if isinstance(self.df[combine["month"]][i], str):

                        abbr_to_num = {name.lower(): num for num, name \
                                      in enumerate(cal.month_abbr) if num}

                        name_to_num = {name.lower(): num for num, name \
                                      in enumerate(cal.month_name) if num}

                        with self.df[combine["month"]][i] as this_month:

                            try:
                                this_month = abbr_to_num[this_month.lower()]

                            except:
                                this_month = name_to_num[this_month.lower()]

                    #print(self.df[i])
                    date = dt.datetime(year=self.df[combine["year"]][i],
                                       month=self.df[combine["month"]][i],
                                       day=self.df[combine["day"]][i])

                    iso_col.append(str(date).replace(' ', 'T') \
                                            .replace(':','')   \
                                            .replace('-',''))

                del self.df[combine["year"]]
                del self.df[combine["month"]]
                del self.df[combine["day"]]

                #self.df["date"] = iso_col
                self.df.insert(loc=0, column="ISO date", value=iso_col)

                self.reshape()

            else:
                datetime = dt.datetime()

        # guess format of the dates and try to make the conversion
        elif cols is not None:

            for c in cols:

                iso_col = []

                for str_date in self.df[c]:
                    iso_col.append(convert_time(str_date))

                self.df[c] = iso_col

        pass


    def shorten(self, data_range=None, stepsize=1, incriment_step_by="day",
                      keep_rows=None):
        '''
        keep_rows is a tuple with (new first row, new second row)
        data_range is a dict {"col_name" : (min, max), ... }
        '''

        # TODO: implement this
        if data_range is not None:

            #first, last = data_range[0], data_range[-1]

            pass

        elif keep_rows is not None:

            first, last = keep_rows[0], keep_rows[-1]

            # new df indexes are [ first , last - 1 ]
            self.df = self.df.drop(self.df.index[:first]) \
                             .drop(self.df.index[last:])  \
                             .reset_index(drop=True)

        if stepsize is not None:
            # call average_each_year and add_each_year

            pass

        self.resize()


    def overlap(self, other, match_cols=None):
        '''
        match_cols is str tuple with columns from each container to match
        call shorten on one or both so they are same size
        '''

        # pick first column and hope for the best
        if match_cols is None:
            match_cols = ("year","year")

        else:
            my_col , your_col = match_cols[0] , match_cols[-1]


        self.df[my_col] = self.df[my_col].astype(str)
        other.df[your_col] = other.df[your_col].astype(str)

        my_col , your_col = match_cols[0] , match_cols[-1]
            
        # func to find overlapping columns and add to the list
        my_vals = set()
        the_list = []
            
        for i,value in self.df.iterrows():
            my_vals.add(self.df[my_col][i])
                
        for i,value in other.df.iterrows():

            if other.df[your_col][i] in my_vals:

                try:
                    the_list.append(other.df[your_col][i])
                except:
                    return

        self.df = self.df[(the_list[0]  <= self.df[my_col]) & \
                          (the_list[-1] >= self.df[my_col])]  \
                          .reset_index(drop=True)

        other.df = other.df[(the_list[0]  <= other.df[your_col]) & \
                            (the_list[-1] >= other.df[your_col])]  \
                            .reset_index(drop=True)

        self.reshape()
        other.reshape()


    def sort_column_by(self, col_name=None, criteria=None): # TODO
        ''' 
        sorts column col_name by specified criteria
        '''

        self.reshape()

        pass


    def average_each_year(self, row=1): # TODO
        '''
        averages values by month or whatever for each year
        TODO: this is incomplete
        '''

        self.reshape()

        pass


    def add_each_year(self, row=1, date_col=None, col_name=None, 
                            extrapolate=False):
        '''
        **RENAME 
        sums all data in same year only for full years, 
        can extrapolate incomplete years (TODO)
        '''

        if col_name is None or date_col is None:

            return 

        temp_dict = {}

        for index, row in self.df.iterrows():

            year = str(row[date_col])[:4]
        
            if year in temp_dict:
                temp_dict[year] += row[col_name]
                
            else:
                temp_dict[year] = row[col_name]

        # could I change this to call self.shorten() ?
        try:
            self.df = pd.DataFrame(list(temp_dict.items()), 
                                   columns=["year",col_name])\
                                  .sort_values(by="year")\
                                  .reset_index(drop=True)

        except AttributeError: # older version\
            print("FYI you should totally update to Pandas >= 0.17.0")
            self.df = pd.DataFrame(list(temp_dict.items()), 
                                   columns=["year",col_name])\
                                  .sort("year")\
                                  .reset_index(drop=True)

        self.reshape()


    def normalize_column(self, col_name=None, zero=False):
        '''
        col_name must be a list 
        normalizes data in a column and adds new column 
        '''

        if isinstance(col_name, str):

            col_name = [col_name]

        for c in col_name:

            temp_col = []

            low , high = self.get_range(column=c)

            if zero == False:
                for index, row in self.df.iterrows():
                    temp_col.append(self.df[c][index]/high)
                
            else:
                for index, row in self.df.iterrows(): # x_i-min / max-min
                    temp_col.append((self.df[c][index] - low) / (high - low))
                    
            self.df["normalized " + c] = temp_col

        self.reshape()


    def combine(self, other, x1=None, x2=None, y1=None, y2=None, zero=False):
        '''
        returns another combined / merged container

        x1 is name of column of independent values for first container
        x2 is name of column of independent values for second container
        y1 is name of column with dependent data of first container
        y2 is name of column with dependent data of second container

        *this is very memory inefficient, but I do not want to change 
         the original containers just in case
        '''

        temp_ct = Container()

        self_copy = self
        other_copy = other

        self_copy.overlap(other_copy, match_cols=(x1, x2))

        temp_ct.df[x1] = self_copy.df[x1]
        temp_ct.df[y1] = self_copy.df[y1]
        temp_ct.df[y2] = other_copy.df[y2]

        temp_ct.normalize_column(col_name=[y1,y2], zero=zero)
        #temp_ct.normalize_column(col_name=y2, zero=zero)

        temp_ct.active = ("normalized " + y1, "normalized " + y2)

        return temp_ct


    def __lt__(self, other):

        return self.size < other.size


    def __le__(self, other):

        return self.size <= other.size


    def __eq__(self, other):

        return self.size == other.size


    def __ne__(self, other):

        return self.size != other.size


    def __gt__(self, other):

        return self.size > other.size


    def __ge__(self, other):

        return self.size >= other.size


    def __repr__(self):
        
        return "Container ({} rows) {}".format(self.size, self.labels)


    def __bool__(self):

        if self.size > 0:
            return True
        else:
            return False

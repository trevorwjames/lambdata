"""
basic functions for cleaning data at outset
"""


def missing_values(df):
    # Function for finding total missing values
    nulls = df.isnull().sum()
    return nulls

"""
basic functions for cleaning data at outset
"""

def missing_values(df):
    nulls = df.isnull().sum()

    return nulls



import pandas as pd
import numpy as np

def preprocess(cyber_C):
    # load the cyber crime datasets
    cyber_C = pd.read_table('cyber_crimes.csv')
    
    # Let's replace the empty strings with NaN values
    cyber_C = cyber_C.replace(' ', np.nan)
    # Let's replace the question marks (?) with NaN values
    cyber_C = cyber_C.replace('?', np.nan)
    # Let's replace the question marks (.) with NaN values
    cyber_C = cyber_C.replace('.', np.nan)
    
    # check for duplicate rows in the dataset -> 
    cyber_C.duplicated().sum()
    
    # check missing values -> 
    cyber_C.isnull().sum()
    
    return cyber_C
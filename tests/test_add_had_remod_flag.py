import sys
sys.path.append('../')

from functions.add_had_remod_flag import *
from functions.import_to_df import *

def test_add_had_remod_flag():
    files = ['train.csv']
    input_data = import_to_df(files)
    input_train_df = input_data['train']

    out_df = add_had_remod_flag(input_train_df)
    flag_mean = out_df.loc[
       out_df['YearRemodAdd'] != out_df['YearBuilt'],
       'HadRemodFlag'
    ].mean()

    assert flag_mean == 1, f"""
        Expecting HadRemodFlag to be 1 in all cases YearRemodAdd != YearBuilt
        Instead its only in {flag_mean * 100: .1f}% of cases
        """
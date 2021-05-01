import sys
sys.path.append('../')

from functions.process_year_remod import *
from functions.import_to_df import *

def test_process_year_remod():
    files = ['train.csv']
    input_data = import_to_df(files)
    input_train_df = input_data['train']

    out_df = process_year_remod(input_train_df)
    grouped_df = (
        out_df
        .groupby('YearRemodPre1950Flag')
        .agg({'YearRemodAdd': ['min', 'mean', 'max']})
    )

    grouped_df.columns = grouped_df.columns.droplevel(0)
    flag_mean = grouped_df.at[1, 'mean']
    assert flag_mean == 1950, f"""
        Expecting the pre 1950 flag to have mean of 1950.
        Instead got {flag_mean}
        """
import sys
sys.path.append('../')

from functions.add_year_remod_pre1950_flag import *
from functions.import_to_df import *

def test_add_year_remod_pre1950_flag():
    files = ['train.csv']
    input_data = import_to_df(files)
    input_train_df = input_data['train']

    out_df = add_year_remod_pre1950_flag(input_train_df)
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
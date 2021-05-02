import sys
sys.path.append('../')

from functions.add_zero_flag import *
from functions.import_to_df import *

def test_add_zero_flag():
    files = ['train.csv']
    input_data = import_to_df(files)
    input_train_df = input_data['train']

    out_df = add_zero_flag(
        data=input_train_df,
        column='MasVnrArea'
        )
    flag_mean = out_df.loc[
       out_df['MasVnrAreaZeroFlag'] == 0,
       'MasVnrArea'
    ].mean()

    assert flag_mean == 0, f"""
        Expecting MaxVnrArea to be 0 in all cases MasVnrAreaZeroFlag is 0.
        Instead its only in {(1 - flag_mean) * 100: .1f}% of cases
        """
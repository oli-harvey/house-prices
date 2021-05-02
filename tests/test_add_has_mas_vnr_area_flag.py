import sys
sys.path.append('../')

from functions.add_has_mas_vnr_area_flag import *
from functions.import_to_df import *

def test_add_has_mas_vnr_area_flag():
    files = ['train.csv']
    input_data = import_to_df(files)
    input_train_df = input_data['train']

    out_df = add_has_mas_vnr_area_flag(input_train_df)
    flag_mean = out_df.loc[
       out_df['hasMasVnrAreaFlag'] == 0,
       'MasVnrArea'
    ].mean()

    assert flag_mean == 0, f"""
        Expecting MaxVnrArea to be 0 in all cases hasMasVnrAreaFlag is 0.
        Instead its only in {(1 - flag_mean) * 100: .1f}% of cases
        """
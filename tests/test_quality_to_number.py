import sys
sys.path.append('../')

from functions.quality_to_number import *
from functions.import_to_df import *

def test_add_zero_flag():
    mock_df = pd.DataFrame({
        'id': [1,2,3,4,5],
        'KitchenQual': ['TA', 'Gd', 'Ex', 'Fa', np.NaN],
    })

    out_df = quality_to_number(
        data=input_train_df,
        column='KitchenQual',
        keep_original=False
        )

    expected_df = pd.DataFrame({
        'id': [1,2,3,4,5],
        'KitchenQual': [3, 4, 5, 2, 0],
    })

    output_order = output_df.columns

    assert mock_df.equals(expected_df[output_order]), f"""
        Expecting MaxVnrArea to be 0 in all cases MasVnrAreaZeroFlag is 0.
        Instead its only in {(1 - flag_mean) * 100: .1f}% of cases
        """
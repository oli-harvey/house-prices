import sys
sys.path.append('../')

from functions.quality_to_number import *
from functions.import_to_df import *
import numpy as np

def test_add_zero_flag():
    mock_df = pd.DataFrame({
        'id': [1,2,3,4,5],
        'KitchenQual': ['TA', 'Gd', 'Ex', 'Fa', np.NaN],
    })

    output_df = quality_to_number(
        data=mock_df,
        column='KitchenQual',
        keep_original=False
        )

    expected_df = pd.DataFrame({
        'id': [1,2,3,4,5],
        'KitchenQualNumber': [3., 4., 5., 2., 0.],
    })

    output_order = output_df.columns

    assert output_df.equals(expected_df[output_order]), f"""
        Not generating numeric version of quality column correctly.
        Got:
        {output_df.head()}
        Expected:
        {expected_df.head()}
        """
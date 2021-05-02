import sys
import numpy as np
sys.path.append('../')

from functions.add_value_dummies_multiple_columns import *
from functions.import_to_df import *

def test_add_value_dummies_multiple_columns():
    mock_df = pd.DataFrame({
        'id': [1,2,3,4,5],
        'BsmtFinType1': ['GLQ', 'ALQ', 'ALQ', 'GLQ', np.NaN],
        'BsmtFinType2': ['Unf', 'Unf', 'GLQ', 'ALQ', np.NaN],
        'BsmtFinSF1': [100, 90, 80, 70, np.NaN],
        'BsmtFinSF2': [0, 0, 30, 0, np.NaN]
    })

    output_df = add_value_dummies_multiple_columns(
            data=mock_df,
            cat_columns=['BsmtFinType1', 'BsmtFinType2'],
            value_columns=['BsmtFinSF1', 'BsmtFinSF2'],
            prefix='BsmtFinTypeSF',
            keep_original=False
        )

    expected_df = pd.DataFrame(
        {
            'id': [1,2,3,4,5],
            'BsmtFinTypeSFGLQ': [100., 0., 30., 70., 0.],
            'BsmtFinTypeSFALQ': [0., 90., 80., 0., 0.],
            'BsmtFinTypeSFUnf': [0., 0., 0., 0., 0.]
        }
    )

    output_order = output_df.columns

    assert output_df.equals(expected_df[output_order]), f"""
        Not generating unique two column summed dummies correctly. 
        Got:
        {output_df.head()}
        Expected:
        {expected_df.head()}
        """
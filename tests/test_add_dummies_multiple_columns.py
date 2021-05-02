import sys
import numpy as np
sys.path.append('../')

from functions.add_dummies_multiple_columns import *
from functions.import_to_df import *

def test_add_dummies_multiple_columns():
    mock_df = pd.DataFrame({
        'id': [1,2,3,4,5],
        'Exterior1st': ['Sand', 'Eggs', 'Brick', 'Spit', np.NaN],
        'Exterior2nd': ['Sand', 'Eggs', 'Sand', 'Brick', np.NaN]
    })

    output_df = add_dummies_multiple_columns(
            data=mock_df,
            columns=['Exterior1st', 'Exterior2nd'],
            prefix='Exterior'
        )
    
    expected_df = pd.DataFrame(
        {
            'id': [1,2,3,4,5],
            'ExteriorSand': [1,0,1,0,0], 
            'ExteriorEggs': [0,1,0,0,0],
            'ExteriorBrick': [0,0,1,1,0],
            'ExteriorSpit': [0,0,0,1,0]
        }
    )

    output_order = output_df.columns

    assert output_df.equals(expected_df[output_order]), f"""
        Not generating unique two column one hots correctly. 
        Got:
        {output_df.head()}
        Expected:
        {expected_df.head()}
        """
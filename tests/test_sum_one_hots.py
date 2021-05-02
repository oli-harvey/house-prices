import sys
import numpy as np
sys.path.append('../')

from functions.sum_onehots import *
from functions.import_to_df import *

def test_sum_one_hots():
    
    mock_df = pd.DataFrame(
        {
            'Id': [1,2,3,4,5],
            'ExteriorSand': [1,0,1,0,0], 
            'ExteriorEggs': [0,1,0,0,0],
            'ExteriorBrick': [0,0,1,1,0],
            'ExteriorSpit': [0,0,0,1,0]
        }
    )

    output_df = sum_onehots(
        data=mock_df,
        prefix='Exterior'
    )
    
    expected_counts = [1,1,2,2,0]
    actual_counts = output_df['ExteriorCount'].tolist()

    assert expected_counts == actual_counts, f"""
        Not summing onehots correctly. These rows are wrong:
        {output_df.loc[output_df['ExteriorCount'] != expected_counts]}
        """
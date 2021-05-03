import sys
sys.path.append('../')

from functions.add_years_since import *
from functions.import_to_df import *
import numpy as np

def test_add_years_since():
    mock_df = pd.DataFrame({
        'id': [1,2,3,4,5],
        'YearBuilt': [1900, 1950, 1970, 2000, np.NaN],
        'YrSold': [2000, 1960, 2000, 1990, np.NaN]
    })

    output_df = add_years_since(
        data=mock_df,
        from_column='YearBuilt',
        to_column='YrSold'
    )
    expected_df = pd.DataFrame({
        'id': [1,2,3,4,5],
        'YearBuilt': [1900, 1950, 1970, 2000, np.NaN],
        'YrSold': [2000, 1960, 2000, 1990, np.NaN],
        'YearsSinceYearBuilt': [100., 10., 30., 0., 0.]
    })

    output_order = output_df.columns

    assert output_df.equals(expected_df[output_order]), f"""
        Not generating years since properly
        Got:
        {output_df.head()}
        Expected:
        {expected_df.head()}
        """
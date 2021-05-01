import sys
sys.path.append('../')

from functions.process_data import *
from functions.import_to_df import *

def test_process_data():
    files = ['train.csv']
    input_data = import_to_df(files)
    input_train_df = input_data['train']

    input_rows = input_train_df.shape[0]

    output_df = process_data(input_train_df)
    output_rows = output_df.shape[0]

    assert isinstance(output_df, pd.DataFrame), f"""
    Expecting to return a DataFrame
    Instead got {type(out_rows)}
    """
   
    assert input_rows == output_rows, f"""
        Expecting the processed DataFrame to have the same rows as input
        Input had {input_rows}
        Output had {output_rows}
        """
import pandas as pd

def add_zero_flag(
        data: pd.DataFrame,
        column: str
        ) -> pd.DataFrame:

    output_df = data.copy()
    flag_name = column + 'ZeroFlag'
    output_df[flag_name] = 1
    output_df.loc[
       output_df[column] == 0,
       flag_name
    ] = 0
    
    return output_df
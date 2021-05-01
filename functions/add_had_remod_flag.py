import pandas as pd

def add_had_remod_flag(
        input_df: pd.DataFrame
        ) -> pd.DataFrame:

    output_df = input_df.copy()
    output_df.loc[
       output_df['YearRemodAdd'] == output_df['YearBuilt'],
       'HadRemodFlag'
    ] = 1
    output_df['HadRemodFlag'].fillna(0)
    
    return output_df
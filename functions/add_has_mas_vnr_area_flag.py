import pandas as pd

def add_has_mas_vnr_area_flag(
        input_df: pd.DataFrame
        ) -> pd.DataFrame:

    output_df = input_df.copy()
    output_df['hasMasVnrAreaFlag'] = 1
    output_df.loc[
       output_df['MasVnrArea'] == 0,
       'hasMasVnrAreaFlag'
    ] = 0
    
    return output_df
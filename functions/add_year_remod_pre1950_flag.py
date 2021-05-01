import pandas as pd

def add_year_remod_pre1950_flag(
        input_df: pd.DataFrame
        ) -> pd.DataFrame:
    output_df = input_df.copy()
    output_df.loc[
        output_df['YearRemodAdd'] <= 1950,
        'YearRemodPre1950Flag'
    ] = 1
    output_df['YearRemodPre1950Flag'].fillna(0, inplace=True)
    return output_df
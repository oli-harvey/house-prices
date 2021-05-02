import pandas as pd

def sum_onehots(
        data: pd.DataFrame,
        prefix: str
        ) -> pd.DataFrame:
    
    output_df = data.copy()

    one_hot_columns = [
       col for col 
       in output_df.columns
       if prefix in col
    ]

    count_col_name = prefix + 'Count'
    output_df[count_col_name] = 0

    for column in one_hot_columns:
        output_df.loc[
            output_df[column] == 1,
            count_col_name
        ] += 1

    return output_df
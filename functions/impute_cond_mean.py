import pandas as pd

def impute_cond_mean(
        df: pd.DataFrame,
        col_with_na: str,
        cond_cols: list
        ) -> pd.DataFrame:

    means_df = (
        df.groupby(cond_cols)
        [col_with_na]
        .mean()
        .reset_index()
    )
    merged_df = df.merge(
        means_df,
        on=cond_cols,
        suffixes=[None, '_imp']
    )
    col_with_na_new_name = col_with_na + '_imp'
    col_with_na_flag_name = col_with_na + 'impute_flag'
    merged_df[col_with_na_flag_name] = 0
    merged_df.loc[merged_df[col_with_na].isna(), col_with_na_flag_name] = 1
    merged_df[col_with_na].fillna(merged_df[col_with_na_new_name], inplace=True)
    
    merged_df.drop(columns=col_with_na_new_name, inplace=True)
    return merged_df

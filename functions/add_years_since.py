import pandas as pd

def add_years_since(
        data: pd.DataFrame,
        from_column: str,
        to_column: str
        ) -> pd.DataFrame:

   output_df = data.copy()
     
   diff_col_name = "YearsSince" + from_column
   output_df[diff_col_name] = output_df[to_column] - output_df[from_column]

   output_df.loc[
      output_df[diff_col_name] < 0,
      diff_col_name
   ] = 0

   output_df[diff_col_name] = output_df[diff_col_name].fillna(0)
    
   return output_df
import pandas as pd
from typing import List

def add_dummies_multiple_columns(
        data: pd.DataFrame,
        columns: List[str],
        prefix: str
        ) -> pd.DataFrame:

   output_df = data.copy()

   levels = set()

   for column in columns:
      values = output_df[column].unique().tolist()
      to_add = [x for x in values if x == x]
      levels.update(to_add)
      # output_df.drop(column, inplace=True, axis=1)

   for level in levels:
      col_name = prefix + level
      output_df[col_name] = 0
      for column in columns:
         output_df.loc[
            output_df[column] == level,
            col_name
         ] = 1
   
   output_df.drop(columns=columns, inplace=True)
   
   return output_df
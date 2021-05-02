import pandas as pd
from typing import List

def add_value_dummies_multiple_columns(
        data: pd.DataFrame,
        cat_columns: List[str],
        value_columns: List[str],
        prefix: str,
        keep_original: bool
        ) -> pd.DataFrame:

   output_df = data.copy()

   pairs_columns = list(zip(cat_columns, value_columns))

   levels = set()

   for column in cat_columns:
      values = output_df[column].unique().tolist()
      to_add = [x for x in values if x == x]
      levels.update(to_add)

   for level in levels:
      col_name = prefix + level
      output_df[col_name] = 0
      for cat, value in pairs_columns:
         output_df.loc[
            output_df[cat] == level,
            col_name
         ] = output_df[value]
   
   if not keep_original:
      all_columns = cat_columns + value_columns
      output_df.drop(columns=all_columns, inplace=True)
   
   return output_df
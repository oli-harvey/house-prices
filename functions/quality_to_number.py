import pandas as pd

def quality_to_number(
        data: pd.DataFrame,
        column: str,
        keep_original: bool = True,
        ) -> pd.DataFrame:

   output_df = data.copy()
     
   quality_dict = {
   # standard ones
   'Ex': 5,
   'Gd': 4,
   'TA': 3,
   'Fa': 2,
   'Po': 1, 
   # basement exposure
   'NA': 0,
   'Av': 3,
   'Mn': 1,
   'No': 0,
   # basement fin type
   'GLQ': 5,
   'ALQ': 3,
   'BLQ': 2,
   'Rec': 3,
   'LwQ': 1,
   'Unf': 0,
   # home functionality
   'Typ': 0,
   'Min1': -1,
   'Min2': -2,
   'Mod': -3,
   'Maj1': -4,
   'Maj2': -5,
   'Sev': -8,
   'Sal': -15
   }
   number_column = column + 'Number'
   output_df[number_column] = output_df[column].map(quality_dict)

   output_df[number_column] = output_df[number_column].fillna(0)

   if not keep_original:
      output_df.drop(columns=[column], inplace=True)
    
   return output_df
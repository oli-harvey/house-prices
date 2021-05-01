import pandas
import os 
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer



funcs = os.listdir('functions')
for func in funcs:
    if func.startswith('__') or func == 'import_all_functions.py':
        continue
    func = func.replace('.py','')
    exec(f'from functions.{func} import *')

def process_data(df: pd.DataFrame) -> pd.DataFrame:
    dummy_cols = []
    impute_cols = ['LotFrontage']
    
    processed_df = df.copy()
    
    # imp = IterativeImputer(max_iter=10, random_state=0)
    processed_df = add_had_remod_flag(processed_df)
    processed_df = add_year_remod_pre1950_flag(processed_df)
    
    return processed_df
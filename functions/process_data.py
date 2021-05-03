import pandas as pd
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
    processed_df = df.copy()

    # drop useless columns. Utilities too sparsely populated to rely on model picking up
    drop_cols = ['Utilities']
    processed_df = processed_df.drop(columns=drop_cols)

    # these ones have values that correspond to the categories so make dummies afterwards but also make these first
    value_dummies = {
        'BsmtFinTypeSF': (['BsmtFinType1', 'BsmtFinType2'], ['BsmtFinSF1', 'BsmtFinSF2'])
    }
    for prefix, col_tuple in value_dummies.items():
        cat_columns, value_columns = col_tuple
        processed_df = add_value_dummies_multiple_columns(
            data=processed_df,
            cat_columns=cat_columns,
            value_columns=value_columns,
            prefix=prefix,
            keep_original=True,
        )

    # convert categorical quality to numeric
    quality_cols_convert = [
        'ExterQual', 'ExterCond', 'BsmtQual', 'BsmtCond', 'BsmtExposure',
        'BsmtFinType1', 'BsmtFinType2', 'HeatingQC', 'KitchenQual', 'Functional',
        'FireplaceQu', 'GarageQual', 'GarageCond', 'PoolQC', 'Fence'
    ]
    for column in quality_cols_convert:
        # first convert to number keeping original column
        processed_df = quality_to_number(
            processed_df,
            column=column,
            keep_original=True,
        )
        # then flag zeros
        number_column = column + 'Number'
        processed_df = add_zero_flag(
            processed_df,
            column=number_column,
        )
    
    # these ones need combining after turning into dummies since values spread over pairs of columns
    dummy_pairs = {
        'Condition': ['Condition1', 'Condition2'],
        'Exterior': ['Exterior1st', 'Exterior2nd'],
        'BsmtFinType': ['BsmtFinType1', 'BsmtFinType2']
    }
    for prefix, columns in dummy_pairs.items():
        processed_df = add_dummies_multiple_columns(
            data=processed_df,
            columns=columns,
            prefix=prefix,
        )

    # create simple dummies
    dummy_cols = ['MSSubClass', 'MSZoning', 'Alley', 'MoSold', 'SaleType']
    # add quality cols as one hots too
    processed_df = pd.get_dummies(processed_df, columns=dummy_cols)

    # flag columns with 0s where useful
    zero_flags = [
        'MasVnrArea', '2ndFlrSF', 'BsmtFinSF1', 'BsmtFinSF2', 'LowQualFinSF', 'GarageYrBlt', 
        'WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch', '3SsnPorch', 'ScreenPorch'
    ]
    for column in zero_flags:
        processed_df = add_zero_flag(
            processed_df,
            column=column,
        )
    
    # calculate years since built and remodAdded
    columns_to_calculate_years_since = [
        ('YearBuilt', 'YrSold'),
        ('YearRemodAdd', 'YrSold'),
    ]
    for from_column, to_column in columns_to_calculate_years_since:
        processed_df = add_years_since(
            data=processed_df,
            from_column=from_column,
            to_column=to_column,
        )

    # deal with remod odd cases. hopefully flagging them is enough
    processed_df = add_had_remod_flag(processed_df)
    processed_df = add_year_remod_pre1950_flag(processed_df)

    # impute missing
    impute_cols = ['LotFrontage']

    # imp = IterativeImputer(max_iter=10, random_state=0)
    # imp.fit(processed_df)
    # processed_df = imp.transform(processed_df)
    
    return processed_df
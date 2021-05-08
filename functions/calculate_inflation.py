from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
import pandas as pd
import functions.import_to_df

def calculate_inflation(
        data_with_price: pd.DataFrame,
        data_to_append_to: pd.DataFrame,
        group_by_cat: [str],
        group_by_band: [str],
        year: str,
        price: int
        ) -> pd.DataFrame:

    group_by_full = [year, *group_by_cat, *group_by_band]
    calc_df = data_with_price.copy()
    out_df = data_to_append_to.copy()
    
    # cont_vars = processed_df.select_dtypes(include=np.number).columns.tolist()
    for col in group_by_band:
        band_col_name = col + '_ntiles'
        cuts = 4
        calc_df[band_col_name] = pd.qcut(
            calc_df[col],
            q=cuts, 
            labels=range(1, cuts+1),
            duplicates='drop'
        )
                
        out_df[band_col_name] = pd.qcut(
            out_df[col],
            q=cuts, 
            labels=range(1, cuts+1),
            duplicates='drop'
        )    
        group_by_full = [
            band_col_name 
            if i == col 
            else i
            for i
            in group_by_full
        ]

    yearly_summary_df = (
        calc_df
            .groupby(group_by_full)
            .agg(AvgPrice = (price, 'mean'))
            .reset_index()
    )
    imp_mean = IterativeImputer(random_state=0)
    imp_mean.fit(yearly_summary_df)
    yearly_summary_df[:] = imp_mean.transform(yearly_summary_df)
    yearly_summary_df.loc[
        yearly_summary_df['AvgPrice'] < 10_000,
        'AvgPrice'
        ] = 10_000
    # move year to end
    group_by_full.remove(year)
    group_by_full = [*group_by_full, year]

    inflation_df = (
        yearly_summary_df
            .groupby(group_by_full)
            .agg(AvgPrice = ('AvgPrice', 'mean'))
            .reset_index()
    )
    inflation_df.columns = [c for c in inflation_df.columns.to_flat_index()]

    start_year = inflation_df.loc[inflation_df[year] == 2006]
    start_year.rename(columns={'AvgPrice': 'BasePrice'}, inplace=True)
    start_year.drop(columns=[year], inplace=True)
    combined_inf_df = inflation_df.merge(
        start_year,
        on=['OverallQual', 'GrLivArea_ntiles']
    )
    combined_inf_df['AvgPrice'] = (
    combined_inf_df
        .groupby(['OverallQual', 'GrLivArea_ntiles'])
        .expanding()
        .agg({'AvgPrice': 'max'})
        .reset_index()
    )['AvgPrice']
    combined_inf_df['Inflation'] = combined_inf_df['AvgPrice'] / combined_inf_df['BasePrice'] 
    combined_inf_df.drop(columns=['BasePrice'], inplace=True)
    out_df = out_df.merge(
        combined_inf_df,
        on=['OverallQual', 'GrLivArea_ntiles', year]
    )
    return out_df
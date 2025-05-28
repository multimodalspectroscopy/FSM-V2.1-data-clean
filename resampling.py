import pandas as pd

def resample_dataframe(df: pd.DataFrame, option: str):
    """
    Resample a DataFrame grouped by 'total_seconds' using the specified method.

    Parameters:
        df (pd.DataFrame): The input DataFrame with a 'total_seconds' column.
        option (str): The resampling option - either 'average' or 'accumulation'.

    Returns:
        tuple: (resampled_df, resample_method_str) or (str, None) if option is invalid.
    """
    if 'total_seconds' not in df.columns:
        return "Error: 'total_seconds' column not found in DataFrame", None

    #Take miliseconds from 'Time' column
    grouped = df.groupby('total_miliseconds')

    if option == 'average':
        resampled_df = grouped.mean(numeric_only=True)
        resample_method_str = "Resampling: Averaging 1Hz"
    elif option == 'accumulation':
        resampled_df = grouped.sum(numeric_only=True)
        resample_method_str = "Resampling: Accumulation 1Hz"
    else:
        return f"Unknown resampling option: {option}", None

    return resampled_df, resample_method_str

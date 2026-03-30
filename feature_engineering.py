import pandas as pd

def feature_engineering(df):
    df = df.copy()

    # Convert dates
    df["Date received"] = pd.to_datetime(df["Date received"], errors="coerce")
    df["Date sent to company"] = pd.to_datetime(df["Date sent to company"], errors="coerce")

    # Create response delay feature
    df["response_delay_days"] = (
        df["Date sent to company"] - df["Date received"]
    ).dt.days

    return df
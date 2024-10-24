def clean_data(df):
    # round the values for GDP to get rid of decimal points
    df['GDP'] = df['GDP'].round()

    return df
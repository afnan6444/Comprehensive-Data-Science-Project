import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.month
    df['Year'] = df['Date'].dt.year
    df['Revenue'] = df['Quantity'] * df['Price']

    for col in ['Product', 'Region', 'Customer_ID']:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
    return df

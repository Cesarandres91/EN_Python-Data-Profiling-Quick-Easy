import pandas as pd
import numpy as np

#Remember edit the path
df = pd.read_csv('PUT_YOUR_DATASET_HERE.csv', header=0)


def data_profiling(df):
    profile = []

    for col in df.columns:
        data = {}
        data['Variable'] = col
        data['Random_Example'] = df[col].dropna().sample(1).values[0] if not df[col].dropna().empty else None
        data['Total_Records'] = df.shape[0]
        data['Nulls'] = df[col].isnull().sum()
        data['Blanks'] = (df[col] == '').sum()
        data['Distinct'] = df[col].nunique()
        if pd.api.types.is_numeric_dtype(df[col]) and not pd.api.types.is_bool_dtype(df[col]):
            data['Max_Value'] = df[col].max()
            data['Min_Value'] = df[col].min()
            data['Range'] = df[col].max() - df[col].min()
            data['Negatives'] = (df[col] < 0).sum()
            data['Positives'] = (df[col] > 0).sum()
            data['Equal_Zero'] = (df[col] == 0).sum()
            data['Average'] = df[col].mean()
            data['Median'] = df[col].median()
            data['Variance'] = df[col].var()
            data['Standard_Deviation'] = df[col].std()
            data['Quartiles'] = df[col].quantile([0.25, 0.5, 0.75]).to_dict()
        else:
            data['Max_Value'] = None
            data['Min_Value'] = None
            data['Range'] = None
            data['Negatives'] = 0
            data['Positives'] = 0
            data['Equal_Zero'] = 0
            data['Average'] = None
            data['Median'] = None
            data['Variance'] = None
            data['Standard_Deviation'] = None
            data['Quartiles'] = None
        if pd.api.types.is_object_dtype(df[col]) or pd.api.types.is_categorical_dtype(df[col]):
            data['Max_Value'] = df[col].value_counts().idxmax()
            data['Min_Value'] = df[col].value_counts().idxmin()
        data['Max_Length'] = df[col].astype(str).apply(len).max()
        data['Min_Length'] = df[col].astype(str).apply(len).min()
        data['Mode'] = df[col].mode()[0] if not df[col].mode().empty else None
        profile.append(data)

    profile_df = pd.DataFrame(profile)
    return profile_df
    

# Generate data profiling
profile_df = data_profiling(df)

# Display the resulting DataFrame in table format
display(profile_df)

# Optional: Export to a CSV file
# profile_df.to_csv('data_profiling.csv', index=False)

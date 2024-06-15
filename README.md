# Python Data Profiling: Quick & Easy
Learning and developing data projects

## Hi there 👋, I'm Cesar (@Cesarandres91)

- 👀 I’m interested in data quality, data science, and data governance.
- 🌱 I’m currently improving my skills in data science.
- 💞️ I’m looking to collaborate on data governance, quality, science or cybersecurity projects.
- 📫 How to reach me: [LinkedIn](https://www.linkedin.com/in/andreschile/)


# Data Profiling Wizard 🧙‍♂️✨

Hello, Data Enthusiasts! Welcome to the **Data Profiling Wizard**, where we turn your data into insights with just a few lines of code! Whether you're a seasoned data scientist or just dipping your toes into the data pool, this tool is designed to make your life easier and a bit more fun! 🎉

## What is Data Profiling? 🤔

Data profiling is the process of examining the data available in an existing data source (e.g., a CSV file) and collecting statistics and information about that data. Why? Because knowing your data inside out helps in understanding its behavior and quality, which are crucial before any data manipulation or analysis.

## Features of the Data Profiling Wizard 🚀

- **Quick Setup:** Get your data profiled in just a couple of steps.
- **Comprehensive Metrics:** From nulls to quartiles—we cover it all.
- **Support for Various Data Types:** Whether it's numeric or categorical, we handle different types of data gracefully.
- **Output Flexibility:** View it on your screen or export it to a CSV file for further analysis.

## How to Use 🛠

### Step 1: Set Up Your Dataset
   Place your dataset file in the same directory as the script, or provide the path to the file.
   ```python
   import pandas as pd
   import numpy as np
   
   # Remember to edit the path
   df = pd.read_csv('PUT_YOUR_DATASET_HERE.csv', header=0)
   ```

### Step 2: Run the Data Profiling Function
   Simply call the `data_profiling()` function with your DataFrame.
   ```python
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
   
   profile_df = data_profiling(df)
   ```

### Step 3: View or Export Your Data Profile

   Display the profiling results directly in your console or notebook.
   ```python
   
   display(profile_df)

  # Optional: Export to a CSV file
  # profile_df.to_csv('data_profiling.csv', index=False)
   ```
## Example of Output 📊

Here's a sneak peek at what the data profile looks like:

| Variable        | Total_Records | Nulls | Distinct | Max_Value | ... |
|-----------------|---------------|-------|----------|-----------|-----|
| Age             | 100           | 0     | 10       | 50        | ... |
| Gender          | 100           | 5     | 2        | Male      | ... |

🚀 Here is a real example with spotify data from Kaggle: https://www.kaggle.com/datasets/asaniczka/top-spotify-songs-in-73-countries-daily-updated

You can find an example of this profiling in this repository under the name: [profiling_data_spotify.csv]


![image](https://github.com/Cesarandres91/Data_profiling_fastandeasy_python/assets/102868086/1af2a3ce-3c72-4f1e-882f-1764c2e64d50)



Fun, right? 🎈

## Requirements 📋

Make sure you have `pandas` and `numpy` installed in your environment:

```bash
pip install pandas numpy
```

## Let the Magic Begin! 🌟

Ready to transform how you understand your data? Clone this repo, follow the setup instructions, and you're good to go! Dive into the magic world of data profiling and uncover the secrets hidden in your data! 🧙‍♂️🔍

---

![image](https://github.com/Cesarandres91/Python-Data-Profiling-Quick-Easy/assets/102868086/57f38228-891e-49d9-857c-d3779e866c84)


Feel free to contribute to this project if you have any cool ideas or improvements. Let's make data profiling fun for everyone!

Happy Profiling! 🎉


## Contribution
To contribute to the project, please follow these steps:
- **Fork the Repository**: Fork the project to your GitHub account.
- **Create a Branch**: Create a branch for your changes.
- **Make Your Changes**: Add or improve functionalities.
- **Submit a Pull Request**: Submit a PR to integrate your changes into the main repository.

## License
This project is licensed under the MIT License - see the `LICENSE` file for more details.



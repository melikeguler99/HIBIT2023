""""MERGE CODE (Folder file to csv files)""""

import pandas as pd
import os
folder_path = '/Users/melike/Desktop/USC_datas'
output_file = '/Users/melike/Desktop/USC_COMBİNED2.csv'
combined_data = pd.DataFrame()
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)
        combined_data = combined_data.append(df, ignore_index=True)
combined_data.to_csv(output_file, index=False)


"""Frequency Histogram of Beta Values by CpgIDs"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

combined_file = '/Users/melike/Desktop/USC_COMBİNED2.csv'  
data = pd.read_csv(combined_file)
beta_columns = data.columns[1:]
plt.figure(figsize=(10, 6))
sns.histplot(data[beta_columns], bins=50, kde=True)
plt.title('Frequency Histogram of Beta Values')
plt.xlabel('Beta Values')
plt.ylabel('Frequency')
plt.show()




"""Distribution of Beta Values by Cancer Type"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats


df = pd.read_csv('/Users/melike/Desktop/Tissue.csv')
beta_columns = df.columns.difference(['Tissue'])

plt.figure(figsize=(12, 6))
sns.boxplot(x='Tissue', y=beta_columns[0], data=df, palette='Set3')
plt.title('Distribution of Beta Values by Cancer Type')
plt.xlabel('Cancer Type')
plt.ylabel('Beta Value')
plt.tight_layout()
plt.show()


"""M value histogram"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/melike/Desktop/df_all (1)_p.csv', header=None)

# Convert the data to float
df = df.apply(pd.to_numeric, errors='coerce')

# Stack the rows into a single column
stacked_data = df.stack()

plt.figure(figsize=(10, 6))
sns.histplot(stacked_data, kde=True, color='skyblue')
plt.xlabel('M-values')
plt.ylabel('Frequency')
plt.title('Distribution of M-values')
plt.grid(axis='y', alpha=0.1)
plt.show()




"""M value histogram"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/melike/Desktop/df_all (1)_p.csv', header=None)

# Convert the data to float
df = df.apply(pd.to_numeric, errors='coerce')

# Stack the rows into a single column
stacked_data = df.stack()

plt.figure(figsize=(10, 6))
sns.histplot(stacked_data, kde=True, color='skyblue')
plt.xlabel('M-values')
plt.ylabel('Frequency')
plt.title('Distribution of M-values')
plt.grid(axis='y', alpha=0.1)
plt.show()



"""Correlation Plot B and M values"""

sns.set_style('whitegrid')

df_M = pd.read_csv('/Users/melike/Desktop/df_all (1)_p.csv')

# Extract beta values from the DataFrame
meta_values = df_M.iloc[:, 1:].values.flatten().astype(float)

df = pd.read_csv('/Users/melike/Desktop/USC_COMBİNED2.csv')
beta_values = df.iloc[:, 1:].values.flatten().astype(float)

# Create a DataFrame containing both beta_values and meta_values
data = pd.DataFrame({'M Values': meta_values,'Beta Values': beta_values})
data.dropna(inplace=True)

plt.figure(figsize=(8, 6))
sns.scatterplot(data=data, x='M Values', y='Beta Values')
plt.title('Relationship between B-Values and M-Values', fontsize=16)
correlation_coefficient = np.corrcoef(data['M Values'], data['Beta Values'])[0, 1]

# Annotate the correlation coefficient on the plot
plt.annotate(f'Correlation Coefficient: {correlation_coefficient:.2f}', 
             xy=(0.05, 0.92), 
             xycoords='axes fraction',
             fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.savefig('cor.png', dpi=300, bbox_inches='tight')
plt.show()
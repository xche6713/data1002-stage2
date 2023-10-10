import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#import data set
df = pd.read_excel("cleandata.xls", "Sheet1")
print(df.head())

#summary analysis
subset_columns = ['infant_whole', 'infant_male', 'infant_female','child_whole', 'child_male', 'child_female']
summary_stats = df[subset_columns].agg(['count', 'mean', 'std', 'min', 'median', 'max']).T
summary_stats.columns = ['Count', 'Mean', 'Standard Deviation', 'Minimum', 'Median', 'Maximum']
print(summary_stats)

#sumamry analysis by region
subset_columns = ['infant_whole', 'infant_male', 'infant_female','child_whole', 'child_male', 'child_female', 'region']
summary_stats = df[subset_columns].groupby('region').agg(['count', 'mean', 'std', 'min', 'median', 'max'])
summary_stats.columns = ['_'.join(col).strip() for col in summary_stats.columns.values]
summary_stats.index.name = 'Region'
print(summary_stats)

#mortality by region and year
average_infant_whole = df.groupby(['region', 'year'])['infant_whole'].mean().reset_index()
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))
sns.barplot(x='year', y='infant_whole', hue='region', data=average_infant_whole, palette='muted')
plt.title('Average Infant Mortality Rate (Whole Population) by Region and Year')
plt.xlabel('Year')
plt.ylabel('Average Infant Whole')
plt.show()

#mortality by region and gender
average_infant_values = df.groupby('region')[['infant_male', 'infant_female']].mean().reset_index()
melted_df = pd.melt(average_infant_values, id_vars='region', value_vars=['infant_male', 'infant_female'], var_name='Gender', value_name='Average Value')
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.barplot(x='region', y='Average Value', hue='Gender', data=melted_df, palette='muted')
plt.title('Average Infant Mortality by Region and Gender')
plt.xlabel('Region')
plt.ylabel('Average Value')
plt.legend(title='Gender')
plt.show()

#infant and child mortality
sns.set(style="whitegrid")
fig, axes = plt.subplots(1, 2, figsize=(14, 6), sharey=True)
sns.scatterplot(x='infant_whole', y='child_male', hue='region', style='year', data=df, ax=axes[0])
sns.regplot(x='infant_whole', y='child_male', data=df, ax=axes[0], scatter=False, color='blue')
axes[0].set_title('Child Male vs Infant Whole')
axes[0].set_xlabel('Infant Whole')
axes[0].set_ylabel('Child Male')
sns.scatterplot(x='infant_whole', y='child_female', hue='region', style='year', data=df, ax=axes[1])
sns.regplot(x='infant_whole', y='child_female', data=df, ax=axes[1], scatter=False, color='green')
axes[1].set_title('Child Female vs Infant Whole')
axes[1].set_xlabel('Infant Whole')
axes[1].set_ylabel('Child Female')
plt.tight_layout()
plt.show()

#distribution of infant mortality rate
sns.set(style="whitegrid")
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
sns.histplot(df['infant_whole'], kde=True, ax=axes[0])
axes[0].set_title('Histogram for Infant Whole')
axes[0].set_xlabel('Infant Whole')
axes[0].set_ylabel('Frequency')
sns.boxplot(y='infant_whole', data=df, ax=axes[1])
axes[1].set_title('Box Plot for Infant Whole')
axes[1].set_ylabel('Infant Whole')
plt.tight_layout()
plt.show()


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = [
    1 if bmi > 25 else 0 for bmi in df['weight'] / ((df['height'] / 100)**2)
]

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = [0 if level == 1 else 1 for level in df['cholesterol']]
df['gluc'] = [0 if level == 1 else 1 for level in df['gluc']]


# Draw Categorical Plot
def draw_cat_plot():
  # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
  df_cat = pd.melt(df,
                   id_vars=['cardio'],
                   value_vars=[
                       'cholesterol', 'gluc', 'smoke', 'alco', 'active',
                       'overweight'
                   ])

  # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
  df_cat['value'] = df_cat['value'].astype(str)
  df_cat = df_cat.groupby(['cardio']).value_counts().reset_index(name='total')
  df_cat = df_cat.sort_values('variable')

  # Draw the catplot with 'sns.catplot()'
  # Get the figure for the output
  fig = sns.catplot(df_cat,
                    x='variable',
                    y='total',
                    col='cardio',
                    kind='bar',
                    errorbar=None,
                    hue='value').fig

  # Do not modify the next two lines
  fig.savefig('catplot.png')
  return fig


# Draw Heat Map
def draw_heat_map():
  # Clean the data
  df_heat = df[(df['ap_lo'] <= df['ap_hi'])
               & (df['height'] >= df['height'].quantile(0.025)) &
               (df['height'] <= df['height'].quantile(0.975)) &
               (df['weight'] >= df['weight'].quantile(0.025)) &
               (df['weight'] <= df['weight'].quantile(0.975))]

  # Calculate the correlation matrix
  corr = df_heat.corr()

  # Generate a mask for the upper triangle
  mask = np.triu(np.ones_like(corr, dtype=bool))

  # Set up the matplotlib figure
  fig, ax = plt.subplots(figsize=(10, 10))

  # Draw the heatmap with 'sns.heatmap()'
  sns.heatmap(corr,
              mask=mask,
              center=0,
              linewidths=.5,
              square=True,
              annot=True,
              fmt='.1f')

  # Do not modify the next two lines
  fig.savefig('heatmap.png')
  return fig

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math
from scipy.stats import yeojohnson

def plot_univariate_analysis(data, feature_cols, plot_type, target=None, hue=None,box_cox=False, figsize=(12, 8)):
    """
    Plot univariate features of a DataFrame using the specified plot type.

    Parameters:
    - df (pd.DataFrame): Input DataFrame.
    - feature_cols (list): List of feature columns to plot.
    - plot_type (str): Type of plot to generate ('box', 'count', or 'kde').
    - target (str): Name of the target variable (optional, required for 'box' plot).
    - hue (str): Name of the variable to use for coloring the plot (optional).
    - figsize (tuple): Figure size (default: (12, 8)).

    Returns:
    - None
    """
    num_features = len(feature_cols)
    # cols = math.ceil(math.sqrt(num_features))
    cols = 3
    rows = math.ceil(num_features / cols)

    fig, axes = plt.subplots(rows, cols, figsize=figsize)
    fig.suptitle(f"{plot_type.capitalize()} Plots of Features", fontsize=16)
    axes = axes.flatten()

    df = data.copy()

    if box_cox:
      df[feature_cols] = df[feature_cols].apply(lambda x: yeojohnson(x)[0],axis=1,result_type='broadcast')
      df.dropna(inplace=True)
      # return df

    for i, feature in enumerate(feature_cols):
        ax = axes[i]

        if plot_type == 'box':
              if hue:
                  sns.boxplot(data=df, y=feature, x=hue, ax=ax)
              else:
                  sns.boxplot(data=df, y=feature, ax=ax)

        elif plot_type == 'count':
            if hue:
                sns.countplot(x=feature, hue=hue, data=df, ax=ax)
            else:
                sns.countplot(x=feature, data=df, ax=ax)

        elif plot_type == 'kde':
            if hue:
                sns.kdeplot(data=df, x=feature, hue=hue, ax=ax)
            else:
                sns.kdeplot(data=df, x=feature, ax=ax)

        ax.set_title(f"{plot_type.capitalize()} Plot: {feature}", fontsize=12)
        ax.set_xlabel(feature)
        ax.set_ylabel("Count")

    # Remove any empty subplots
    if len(feature_cols) < rows * cols:
        for j in range(len(feature_cols), rows * cols):
            fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()

    

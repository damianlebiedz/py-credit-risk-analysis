import matplotlib.pyplot as plt
import seaborn as sns
from seaborn import set_theme

set_theme(style="whitegrid")  # Konfiguracja stylu wykresów

def plot_histograms(df):
    """Plot histograms for numerical features."""
    num_columns = df.select_dtypes(include=['float64', 'int64']).columns
    df[num_columns].hist(bins=15, figsize=(15, 10), color='steelblue', edgecolor='black')
    plt.suptitle('Histogram of Numerical Features')
    plt.show()

def plot_target_distribution(df):
    """Plot distribution of target variable."""
    sns.countplot(x='target', data=df, palette='viridis')
    plt.title('Distribution of Target Variable')
    plt.xlabel('Target')
    plt.ylabel('Count')
    plt.show()

def plot_correlation_matrix(df):
    """Plot correlation matrix for the dataset."""
    correlation_matrix = df.corr()
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix')
    plt.show()
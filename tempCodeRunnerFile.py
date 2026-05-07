# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import shapiro, ttest_ind
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant


# %%
# Load the dataset (replace 'your_data.csv' with your actual data file)
df = pd.read_csv('cleaned_data.csv')

# Basic data exploration
print("Dataset Shape:", df.shape)
print("\nMissing Values:\n", df.isnull().sum())
print("\nData Types:\n", df.dtypes)

# %%
def categorize_sales(df, sales_column='total_sales'):
    """
    Categorize games into Low, Medium, and High sales based on percentiles
    
    Args:
        df: DataFrame containing the sales data
        sales_column: Name of the column containing sales data
        
    Returns:
        Series containing sales categories
    """
    # Calculate percentile thresholds
    low_threshold = df[sales_column].quantile(0.333)
    high_threshold = df[sales_column].quantile(0.666)
    
    # Create categories
    def assign_category(x):
        if x <= low_threshold:
            return 'Low'
        elif x <= high_threshold:
            return 'Medium'
        else:
            return 'High'
    
    return df[sales_column].apply(assign_category)

# Add sales categories to the dataframe
df['sales_category'] = categorize_sales(df)

# Display distribution of sales categories
print("\nSales Category Distribution:")
print(df['sales_category'].value_counts())

# Show summary statistics for each category
print("\nSales Statistics by Category:")
print(df.groupby('sales_category')['total_sales'].describe())

# Display example games from each category
print("\nExample Games from Each Category:")
for category in ['Low', 'Medium', 'High']:
    print(f"\n{category} Sales Examples:")
    print(df[df['sales_category'] == category][['sales_category', 'total_sales', 'sales_category']].head(3))

# Create a box plot to visualize sales distribution by category
plt.figure(figsize=(10, 6))
sns.boxplot(x='sales_category', y='total_sales', data=df)
plt.title('Sales Distribution by Category')
plt.show()

# %% [markdown]
# # Data Analysis and Sales Metrics

# %%


# Handle missing values and create sales metrics
def analyze_sales_and_genres(df):
    """
    Perform sales analysis and genre-based grouping
    
    Args:
        df: DataFrame containing game data
    """
    # Make a copy to avoid modifying original data
    df_analysis = df.copy()
    
    # Handle missing values
    df_analysis.fillna(method='ffill', inplace=True)
    
    # Calculate sales percentage contribution
    df_analysis['sales_percentage'] = (df_analysis['total_sales'] / 
                                     df_analysis['total_sales'].sum()) * 100
    
    # Display sales metrics
    print("\nSales Metrics (First 5 Games):")
    print(df_analysis[['total_sales', 'sales_percentage']].head())
    
    # Group by genre and calculate average critic score
    genre_stats = df_analysis.groupby('genre').agg({
        'critic_score': 'mean',
        'total_sales': 'sum',
        'sales_percentage': 'sum'
    }).round(2)
    
    print("\nGenre Statistics:")
    print(genre_stats.sort_values('total_sales', ascending=False))
    
    # Find top 10 best-selling games
    top10_games = df_analysis.nlargest(10, 'total_sales')
    print("\nTop 10 Best-Selling Games:")
    display_columns = ['title', 'genre', 'total_sales', 'sales_percentage']
    print(top10_games[display_columns])
    
    # Visualize genre performance
    plt.figure(figsize=(12, 6))
    sns.barplot(data=genre_stats.reset_index(), 
                x='genre', 
                y='total_sales',
                order=genre_stats.sort_values('total_sales', ascending=False).index)
    plt.xticks(rotation=45)
    plt.title('Total Sales by Genre')
    plt.tight_layout()
    plt.show()

# Run the analysis
analyze_sales_and_genres(df)

# %%
# 1. Bar Chart - Top 5 Publishers
plt.figure(figsize=(12, 6))
top5_publishers = df.groupby('publisher')['total_sales'].sum().nlargest(5)
sns.barplot(x=top5_publishers.index, y=top5_publishers.values)
plt.title('Top 5 Publishers by Total Sales')
plt.xlabel('Publisher')
plt.ylabel('Total Sales (millions)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# %%
# 2. Histogram - Critic Scores Distribution
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='critic_score', bins=30, kde=True)
plt.title('Distribution of Critic Scores')
plt.xlabel('Critic Score')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# %%
# 3. Scatter Plot - Critic Score vs Sales
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='critic_score', y='total_sales', alpha=0.5)
plt.title('Relationship between Critic Scores and Total Sales')
plt.xlabel('Critic Score')
plt.ylabel('Total Sales (millions)')
plt.tight_layout()
plt.show()

# %%
# 4. Pie Chart - Regional Sales Distribution
plt.figure(figsize=(10, 8))
regional_sales = df[['na_sales', 'pal_sales', 'jp_sales', 'other_sales']].sum()
plt.pie(regional_sales, labels=regional_sales.index, autopct='%1.1f%%')
plt.title('Regional Sales Distribution')
plt.axis('equal')
plt.show()

# %%
# 5. Correlation Heatmap
plt.figure(figsize=(12, 8))
numeric_cols = ['critic_score', 'total_sales', 'na_sales', 'pal_sales', 'jp_sales', 'other_sales']
correlation_matrix = df[numeric_cols].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Heatmap of Sales and Ratings')
plt.tight_layout()
plt.show()

# %%
# 2. Outlier Analysis with Box Plots
plt.figure(figsize=(12, 6))
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
# Sales outliers
sns.boxplot(y='total_sales', data=df, ax=ax1, color='violet')
ax1.set_title('Outliers in Total Sales')
    
# Critic score outliers
sns.boxplot(y='critic_score', data=df, ax=ax2, color='lightblue')
ax2.set_title('Outliers in Critic Scores')
    
plt.tight_layout()
plt.show()

# %%
# 4. Genre Distribution Analysis
plt.figure(figsize=(12, 6))
genre_counts = df['genre'].value_counts()
sns.barplot(x=genre_counts.index, y=genre_counts.values, color='orange')
plt.title('Distribution of Game Genres')
plt.xlabel('Genre')
plt.ylabel('Number of Games')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
    

# %%


# %%


# %%


# %%




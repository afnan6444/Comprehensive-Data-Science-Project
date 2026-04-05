import matplotlib.pyplot as plt
import seaborn as sns

def plot_sales_trend(df):
    plt.figure(figsize=(10,6))
    sns.lineplot(x="Date", y="Total_Sales", data=df)
    plt.title("Sales Trend Over Time")
    plt.show()

def plot_region_sales(df):
    plt.figure(figsize=(8,5))
    sns.barplot(x="Region", y="Total_Sales", data=df)
    plt.title("Sales by Region")
    plt.show()

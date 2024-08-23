import matplotlib.pyplot as plt
import seaborn as sns

def plot_data(df, x, y, kind='line'):
    if kind == 'line':
        df.plot(x=x, y=y)
    elif kind == 'bar':
        df.plot.bar(x=x, y=y)
    plt.show()

def plot_distribution(df, column):
    sns.histplot(df[column], kde=True)
    plt.show()

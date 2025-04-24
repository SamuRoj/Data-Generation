import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter

def graph_categories(df):
    categories_data = df.loc[:, "Category"]
    categories_data = Counter(categories_data)
    labels = list(categories_data.keys())
    values = list(categories_data.values())
    plt.pie(values, labels=labels, autopct="%.2f%%")
    plt.show()

def graph_tiers(df):
    tier_data = df.loc[:, "Tier"]
    tier_data = Counter(tier_data)
    labels = list(tier_data.keys())
    values = list(tier_data.values())
    plt.pie(values, labels=labels, autopct="%.2f%%")
    plt.show()

def graph_brand(df):
    brand_data = df.loc[:, "Brand"]
    brand_data = Counter(brand_data)
    labels = list(brand_data.keys())
    values = list(brand_data.values())
    values.sort()

    plt.barh(labels, values)
    plt.xlabel("Cantidad de compras")
    plt.ylabel("Marcas")
    plt.title("Cantidad de compras por marca")

    plt.show()



def graphics():
    df = pd.read_csv("data.csv")
    df.set_index("Sale Id")
    graph_categories(df)
    graph_tiers(df)
    graph_brand(df)

graphics()
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from collections import Counter

def graph_categories(df):
    categories_data = df.loc[:, "Category"]
    categories_data = Counter(categories_data)
    labels = list(categories_data.keys())
    values = list(categories_data.values())
    plt.pie(values, labels=labels, autopct="%.2f%%")
    plt.title("Porcentaje de compra según categoría.")
    plt.show()

def graph_tiers(df):
    tier_data = df.loc[:, "Tier"]
    tier_data = Counter(tier_data)
    labels = list(tier_data.keys())
    values = list(tier_data.values())
    plt.pie(values, labels=labels, autopct="%.2f%%")
    plt.title("Porcentaje de compra por gama.")
    plt.show()

def graph_brand(df):
    brand_data = df.loc[:, "Brand"]
    brand_data = Counter(brand_data)
    brand_data = dict(sorted(brand_data.items(), key=lambda item: item[1]))
    labels = list(brand_data.keys())
    values = list(brand_data.values())

    plt.barh(labels, values)
    plt.xlabel("Cantidad de compras")
    plt.ylabel("Marcas")
    plt.title("Cantidad de compras por marca")

    plt.show()

def graph_mobile_price(df):
    df = df[df["Category"] == "Mobile"] 
    plt.hist(df["Price (USD)"], bins=15)
    plt.xlabel("Precio de celulares")
    plt.ylabel("Cantidad de celulares")
    plt.title("Celulares comprados por precio")
    plt.show()

def graph_laptop_price(df):
    df = df[df["Category"] == "Laptop"] 
    plt.hist(df["Price (USD)"], bins=15)
    plt.xlabel("Precio de laptops")
    plt.ylabel("Cantidad de laptops")
    plt.title("Laptops compradas por precio")
    plt.show()

def graph_customer_age(df):
    plt.hist(df["Customer Age"], bins=20, density=True, label="Customer Age", alpha=0.6)

    mean = df["Customer Age"].mean()
    std = df["Customer Age"].std()
    x = np.linspace(17, 61, 500)
    y = (1 / (std * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std) ** 2)
    plt.plot(x, y, color="red", label="Normal Dist: µ = 30, σ = 5", linestyle="--")

    plt.xlabel("Edad cliente")
    plt.ylabel("Cantidad de clientes")
    plt.title("Edades de los clientes")
    plt.legend()

    plt.show()

def graph_screen_size_mobile(df):
    df = df[df["Category"] == "Mobile"]
    plt.hist(df["Screen Size"], bins=20)
    plt.xlabel("Tamaños de pantalla")
    plt.title("Frecuencia de tamaños de pantalla de celular")
    plt.show()

def graph_screen_size_laptop(df):
    df = df[df["Category"] == "Laptop"]
    plt.hist(df["Screen Size"], bins=20)
    plt.xlabel("Tamaños de pantalla")
    plt.title("Frecuencia de tamaños de pantalla de laptop")
    plt.show()

def graph_gender(df):
    gender_data = df.loc[:, "Customer Gender"]
    gender_data = Counter(gender_data)
    labels = list(gender_data.keys())
    values = list(gender_data.values())
    plt.pie(values, labels=labels, autopct="%.2f%%")
    plt.title("Porcentaje de cliente según género")
    plt.show()

def graph_payment_method(df):
    payment_method_data = df.loc[:, "Payment Method"]
    payment_method_data = Counter(payment_method_data)
    payment_method_data = dict(sorted(payment_method_data.items(), key=lambda item: item[1]))
    labels = list(payment_method_data.keys())
    values = list(payment_method_data.values())

    plt.barh(labels, values)
    plt.xlabel("Cantidad")
    plt.ylabel("Métodos de pago")
    plt.title("Uso de métodos de pago")

    plt.show()

def graph_rating(df):
    rating_data = df.loc[:, "Rating"]
    rating_data = Counter(rating_data)
    rating_data = dict(sorted(rating_data.items(), key=lambda item: item[0]))
    labels = list(rating_data.keys())
    values = list(rating_data.values())
    plt.pie(values, labels=labels, autopct="%.2f%%")
    plt.title("Porcentaje de calificaciones de clientes")
    plt.show()

def graph_quantities(df):
    plt.hist(df["Quantity Sold"], bins = 5)
    plt.xlabel("Cantidad comprada")
    plt.ylabel("Número de productos")
    plt.title("Cantidad de dispositivos por transacción")
    plt.show()

def graphics():
    df = pd.read_csv("data.csv")
    df.set_index("Sale Id")
    graph_categories(df)
    graph_tiers(df)
    graph_brand(df)
    graph_mobile_price(df)
    graph_laptop_price(df)
    graph_screen_size_mobile(df)
    graph_screen_size_laptop(df)
    graph_quantities(df)
    graph_customer_age(df)
    graph_gender(df)
    graph_payment_method(df)
    graph_rating(df)

graphics()
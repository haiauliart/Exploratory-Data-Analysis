#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")


# In[3]:


print(order_df.shape)


# In[4]:


print(order_df.head(10))


# In[5]:


# Quick summary  dari segi kuantitas, harga, freight value, dan weight
print(order_df.describe())
# Median median dari total pembelian konsumen per transaksi kolom price
print(order_df.loc[:, "price"].median())


# In[11]:


import matplotlib.pyplot as plt
# plot histogram kolom: price
order_df[["price"]].plot.hist(figsize=(4, 5), bins=10, xlabelsize=8, ylabelsize=8)
# Untuk menampilkan histogram plot
plt.show()  


# In[13]:


# Standar variasi kolom product_weight_gram
order_df.loc[:, "product_weight_gram"].std()
# Varians kolom product_weight_gram
order_df.loc[:, "product_weight_gram"].var()


# In[14]:


# Hitung quartile 1
Q1 = order_df[["product_weight_gram"]].quantile(0.25)
# Hitung quartile 3
Q3 = order_df[["product_weight_gram"]].quantile(0.75)
# Hitung inter quartile range dan cetak ke console
IQR = Q3 - Q1
print(IQR)


# In[15]:


# Ganti nama kolom freight_value menjadi shipping_cost
order_df.rename(columns={"freight_value" : "shipping_cost"}, inplace=True)
print(order_df)


# In[16]:


# Hitung rata rata dari price per payment_type
rata_rata = order_df["price"].groupby(order_df["payment_type"]).mean()
print(rata_rata)


# In[12]:


# Hitung harga maksimum pembelian customer
sort_harga = order_df.sort_values(by="price", ascending=True)
print(sort_harga)


# In[21]:


# Median price yang dibayar customer dari masing-masing metode pembayaran. 
median_price = order_df["price"].groupby(order_df["quantity"]).median()
print(median_price)


# In[11]:


# Ubah freight_value menjadi shipping_cost dan cari shipping_cost 
# termahal dari data penjualan tersebut menggunakan sort.
import pandas as pd
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")
order_df.rename(columns={"freight_value": "shipping_cost"}, inplace=True)
sort_value = order_df.sort_values(by="shipping_cost", ascending=0)
print(sort_value)


# In[10]:


# Untuk product_category_name, berapa  rata-rata weight produk tersebut 
# dan standar deviasi mana yang terkecil dari weight tersebut, 
import pandas as pd
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")
mean_value = order_df["product_weight_gram"].groupby(order_df["product_category_name"]).mean()
print(mean_value.sort_values())
std_value = order_df["product_weight_gram"].groupby(order_df["product_category_name"]).std()
print(std_value.sort_values())


# In[5]:


import pandas as pd
order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")


# In[6]:


print(order_df.shape)


# In[8]:


# Buat histogram quantity penjualan dari dataset tersebutuntuk melihat persebaran quantity 
# penjualan tersebut dengan bins = 5 dan figsize= (4,5)
import matplotlib.pyplot as plt
order_df[["quantity"]].hist(figsize=(4, 5), bins=5)
plt.show()


# In[ ]:





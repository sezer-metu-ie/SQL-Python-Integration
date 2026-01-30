import pyodbc
import pandas as pd

# 1. SQL Server'a Bağlantı Kuruyoruz
# Not: Sunucu adın SQL ekranında gördüğümüz üzere .\SQLEXPRESS01
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'SERVER=.\\SQLEXPRESS01;'
                      'DATABASE=BusinessAnalytics;'
                      'Trusted_Connection=yes;')

# 2. SQL'deki Tabloyu Pandas'a Aktarıyoruz
query = "SELECT * FROM SalesData"
df = pd.read_sql(query, conn)

# 3. Akıllı Analiz: Toplam Satış Tutarını Hesaplayalım
df['Toplam_Kazanc'] = df['Price'] * df['Quantity']

# 4. Sonuçları Ekrana Basalım
print("--- SQL Server'dan Çekilen Ham Veri ---")
print(df)
print("\n--- Ürün Bazlı Performans Raporu ---")
print(df[['Product', 'Quantity', 'Toplam_Kazanc']])

# Bağlantıyı kapatalım
conn.close()
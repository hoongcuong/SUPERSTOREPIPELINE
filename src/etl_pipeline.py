import requests
import pandas as pd

def extract_from_api():
    url = "https://v6.exchangerate-api.com/v6/2de11a29b893a9c53ede5688/latest/USD"
    response = requests.get(url)
    data = response.json()
    if data["result"] == "success":
        exchange_rate = data["conversion_rates"]["VND"]
        print(f"Exchange Rate USD -> VND: {exchange_rate}")
        return exchange_rate
    else:
        raise Exception("API call failed!")

def extract_from_csv(file_path):
    df = pd.read_csv(file_path, encoding='latin1')
    print(f"Loaded {len(df)} rows from CSV")
    return df

# Test
csv_data = extract_from_csv("superstore.csv")
exchange_rate = extract_from_api()

def transform_data(csv_data, exchange_rate):
    # Làm sạch dữ liệu
    csv_data.dropna(subset=['Sales', 'Order Date'], inplace=True)
    csv_data['Order Date'] = pd.to_datetime(csv_data['Order Date'])
    
    # Tính toán doanh thu điều chỉnh
    csv_data['Total_Sales_USD'] = csv_data['Sales']
    csv_data['Total_Sales_VND'] = csv_data['Sales'] * exchange_rate
    
    # Chuẩn hóa cột
    csv_data['Category'] = csv_data['Category'].str.title()
    csv_data['Region'] = csv_data['Region'].str.title()
    
    return csv_data

# Test
transformed_data = transform_data(csv_data, exchange_rate)
print("Transformed Data Sample:\n", transformed_data[['Order Date', 'Category', 'Region', 'Sales', 'Total_Sales_VND']].head())

import pandas as pd
import requests
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns

# Extract
def extract_from_csv(file_path):
    return pd.read_csv(file_path, encoding='latin1')

def extract_from_api():
    api_key = "2de11a29b893a9c53ede5688"
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["conversion_rates"]["VND"]
    else:
        raise Exception(f"API call failed: {response.status_code}")

# Transform
def transform_data(csv_data, exchange_rate):
    csv_data.dropna(subset=['Sales', 'Order Date'], inplace=True)
    csv_data['Order Date'] = pd.to_datetime(csv_data['Order Date'])
    csv_data['Total_Sales_USD'] = csv_data['Sales']
    csv_data['Total_Sales_VND'] = csv_data['Sales'] * exchange_rate
    csv_data['Category'] = csv_data['Category'].str.title()
    csv_data['Region'] = csv_data['Region'].str.title()
    return csv_data

# Load
def load_data(df):
    try:
        engine = create_engine("postgresql+psycopg2://postgres:123456@localhost:5433/sales_db")
        df_selected = df[['Order ID', 'Product Name', 'Category', 'Quantity', 'Sales', 'Order Date', 'Region', 'Total_Sales_VND']]
        df_selected.columns = ['order_id', 'product_name', 'category', 'quantity', 'sales_usd', 'order_date', 'region', 'total_sales_vnd']
        df_selected.to_sql("sales_table", engine, if_exists="replace", index=False)
        print("Data loaded to PostgreSQL successfully!")
    except Exception as e:
        print(f"Error connecting to PostgreSQL: {e}")

# Analyze & Visualize
def analyze_data(df):
    sales_by_product = df.groupby('Product Name')['Total_Sales_VND'].sum()
    sales_by_region = df.groupby('Region')['Total_Sales_VND'].sum()
    sales_by_date = df.groupby(df['Order Date'].dt.date)['Total_Sales_VND'].sum()
    return sales_by_product, sales_by_region, sales_by_date

def visualize_data(product, region, date):
    plt.figure(figsize=(12, 6))
    sns.barplot(x=product.index[:10], y=product.values[:10], hue=product.index[:10], palette="Blues_d", legend=False)
    plt.title("Top 10 Doanh Thu Theo Sản Phẩm (VND)", fontsize=14)
    plt.xlabel("Sản phẩm", fontsize=12)
    plt.ylabel("Doanh thu (VND)", fontsize=12)
    plt.xticks(rotation=45)
    plt.savefig("sales_by_product.png", dpi=300)
    plt.close()

    plt.figure(figsize=(8, 8))
    plt.pie(region, labels=region.index, autopct="%1.1f%%", colors=sns.color_palette("Set2"))
    plt.title("Phân Bố Doanh Thu Theo Khu Vực", fontsize=14)
    plt.savefig("sales_by_region.png", dpi=300)
    plt.close()

    plt.figure(figsize=(10, 6))
    date.plot(kind="line", marker="o", color="teal")
    plt.title("Doanh Thu Theo Ngày (VND)", fontsize=14)
    plt.xlabel("Ngày", fontsize=12)
    plt.ylabel("Doanh thu (VND)", fontsize=12)
    plt.savefig("sales_by_date.png", dpi=300)
    plt.close()

# Main
if __name__ == "__main__":
    csv_data = extract_from_csv("superstore.csv")
    exchange_rate = extract_from_api()
    transformed_data = transform_data(csv_data, exchange_rate)
    load_data(transformed_data)
    product, region, date = analyze_data(transformed_data)
    visualize_data(product, region, date)
    print("Pipeline completed successfully!")

    
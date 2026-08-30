import pandas as pd
import matplotlib.pyplot as plt
# 1. READ THE CSV FILE
df = pd.read_csv("sales_data.csv")
# Convert Date into date format
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
#2.CALCULATE SALES
df["Sales"] = df["Quantity"] * df["Price"]
#3.CALCULATE PROFIT
df["Profit"] = (df["Price"] - df["Cost"]) * df["Quantity"]
#4.BASIC SALES ANALYSIS
print("================================")
print("       SALES ANALYSIS")
print("================================")
total_sales = df["Sales"].sum()
print("Total Sales: ₹", total_sales)
total_quantity = df["Quantity"].sum()
print("Total Products Sold:", total_quantity)
total_profit = df["Profit"].sum()
print("Total Profit: ₹", total_profit)
#5. PRODUCT ANALYSIS
product_quantity = df.groupby("Product")["Quantity"].sum()
print("\n===== PRODUCTS SOLD =====")
print(product_quantity)
# Most sold product
most_sold = product_quantity.idxmax()
print("\nMost Sold Product:", most_sold)
# Sales made by each product
product_sales = df.groupby("Product")["Sales"].sum()
print("\n===== SALES BY PRODUCT =====")
print(product_sales)
# Product that made the most money
best_product = product_sales.idxmax()
print("\nBest Revenue Product:", best_product)
# 6. CITY ANALYSIS
city_sales = df.groupby("City")["Sales"].sum()
print("\n===== SALES BY CITY =====")
print(city_sales)
# Best city
best_city = city_sales.idxmax()
print("\nBest City:", best_city)
# 7. CUSTOMER ANALYSIS
customer_sales = df.groupby("Customer")["Sales"].sum()
print("\n===== SALES BY CUSTOMER =====")
print(customer_sales)
# Best customer
best_customer = customer_sales.idxmax()
print("\nBest Customer:", best_customer)
# 8. MONTHLY SALES
df["Month"] = df["Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Sales"].sum()
print("\n===== MONTHLY SALES =====")
print(monthly_sales)
# 9. BEST MONTH
best_month = monthly_sales.idxmax()
print("\nBest Month:", best_month)
# 10. DAILY SALES
daily_sales = df.groupby("Date")["Sales"].sum()
print("\n===== DAILY SALES =====")
print(daily_sales)
# 11. PRODUCT SALES GRAPH
plt.figure(figsize=(8, 5))
product_sales.plot(kind="bar")
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()
# 12. CITY SALES GRAPH
plt.figure(figsize=(8, 5))
city_sales.plot(kind="bar")
plt.title("Sales by City")
plt.xlabel("City")
plt.ylabel("Sales")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()
# 13. MONTHLY SALES GRAPH
plt.figure(figsize=(8, 5))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()
# 14. DAILY SALES GRAPH
plt.figure(figsize=(10, 5))
daily_sales.plot(kind="line", marker="o")
plt.title("Daily Sales")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# 15. FINAL SUMMARY
print("\n================================")
print("        FINAL SUMMARY")
print("================================")
print("Total Sales: ₹", total_sales)
print("Total Profit: ₹", total_profit)
print("Total Products Sold:", total_quantity)
print("Most Sold Product:", most_sold)
print("Best Revenue Product:", best_product)
print("Best City:", best_city)
print("Best Customer:", best_customer)
print("Best Month:", best_month)
print("\nProject Completed Successfully!")
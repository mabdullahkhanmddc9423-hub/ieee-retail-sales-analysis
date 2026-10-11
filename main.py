import pandas as pd
import numpy as np

def main():
    # Step 1: Load dataset from csv file
    csv_path = 'data/sales.csv'
    print(f"Loading dataset from {csv_path}......")

    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        print(f"Error: The file '{csv_path}' was not found. Please place your file inside the 'data/' folder.")
        return  

    # Step 2: Data cleaning and handling Missing/Invalid values
    initial_rowcount = len(df)
    
    # Remove duplicate transaction records based on 'order_id'
    df = df.drop_duplicates(subset=['order_id'])
    
    # Coerce non-numeric text entries in numeric columns to NaN (Fixed column names)
    df['units_sold'] = pd.to_numeric(df['units_sold'], errors='coerce')
    df['unit_price'] = pd.to_numeric(df['unit_price'], errors='coerce')
    
    # Impute missing values (fill missing quantities with median and prices with mean)
    df['units_sold'] = df['units_sold'].fillna(df['units_sold'].median())
    df['unit_price'] = df['unit_price'].fillna(df['unit_price'].mean())
    
    print(f"Data cleaned: Processed {initial_rowcount} rows, removed duplicates/invalid entries")
    
    # Step 3: NumPy Revenue Calculations
    df['revenue'] = df['units_sold'] * df['unit_price']
    
    # Convert Pandas series to NumPy arrays for fast statistical computations
    revenues_np = df['revenue'].to_numpy()
    units_np = df['units_sold'].to_numpy()

    total_revenue = np.sum(revenues_np)        
    total_units_sold = np.sum(units_np)
    total_orders = len(df)
    avg_order_value = total_revenue / total_orders if total_orders > 0 else 0  # Fixed variable name

    # Step 4: Groupby & Business Insights
    category_summary = df.groupby('category')['revenue'].sum().reset_index()
    category_summary = category_summary.sort_values(by='revenue', ascending=False)

    # Group by product name to find top performers
    product_summary = df.groupby('product_name')['revenue'].sum().reset_index()
    product_summary = product_summary.sort_values(by='revenue', ascending=False)
    top_product = product_summary.iloc[0]['product_name'] if not product_summary.empty else "N/A"

    # Regional sales breakdown
    region_summary = df.groupby('region')['revenue'].sum().reset_index()
    region_summary = region_summary.sort_values(by='revenue', ascending=False)

    # Step 5: Clean Console Business Summary Report
    print("\n" + "=" * 60)
    print("   Retail Sales Intelligence - Summary Report   ")
    print("=" * 60)
    print(f"Total Revenue          : ${total_revenue:,.2f}")
    print(f"Total Units Sold       : {total_units_sold:,}")
    print(f"Total Valid Orders     : {total_orders}")
    print(f"Average Order Value    : ${avg_order_value:,.2f}")
    print(f"Top-Performing Product : {top_product}")
    print("-" * 55)
    
    print("\n[Revenue Breakdown by Category]")
    print(category_summary.to_string(index=False))
    
    print("\n[Regional Sales Performance]")
    print(region_summary.to_string(index=False))
    print("=" * 55)

if __name__ == '__main__':
    main()
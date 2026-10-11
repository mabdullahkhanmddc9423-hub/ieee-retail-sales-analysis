# Retail Sales Intelligence
### IEEE LGU AI/ML Cohort One - Fall 2026
**Week 3 Assignment:** Data Analysis with NumPy and Pandas
**AI/ML Leads:** Abdullah Faisal & Alina Irshad

## 1. Project Overview
This project analyzes a raw retail sales dataset containing multiple product transactions across different regions. The program processes and cleans the data to generate a business intelligence report highlighting total revenue, average order value, top-performing products, and regional sales breakdowns.
## 2. Key Concepts Implemented
- [x] Pandas DataFrame Loading & Cleaning ('read_csv', 'fillna', 'dropna', 'drop_duplicates')
- [x] NumPy Statistical Calculations (Mean, Median, Standard Deviation, Sums)
- [x] Data Grouping & Aggregation ('groupby')
- [x] Conditional Filtering & Indexing
- [x] Dataset Merging / Time-Series Resampling (if applicable)
## 3. How to run the program
python main.py
## 4. Dataset Information & Cleaning Decisions
Data Source: Custom retail sales CSV dataset created with 25-30 records containing intentional noise, stored in the data/sales.csv file.   
Missing Values & Cleaning: Dropped duplicate transaction rows based on order_id to ensure unique records.
Handled missing or non-numeric quantities and prices by filling or dropping corrupted rows to maintain mathematical accuracy.
## 5. Console Output Screenshots
Terminal Output:
![Terminal Output](ieee-retail-sales-analysis/Program1.png)

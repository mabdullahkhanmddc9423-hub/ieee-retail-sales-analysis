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

### Terminal Output and Summary report:
<img width="701" height="50" alt="cleaningoutput" src="https://github.com/user-attachments/assets/0a72a98c-deb9-4cfe-a0ab-ee9f9c571466" />
<img width="997" height="553" alt="summaryreport" src="https://github.com/user-attachments/assets/a9ff3073-5e6b-4e89-901f-4ff9aa62326e" />

### Description
The business generated a Total Revenue of $3,492.81 across 25 valid orders with an Average Order Value of $139.71, moving a total of 81 units.   
Top Product: Office Chair emerged as the highest-performing product.   
Category Breakdown: Electronics led total sales ($1,880.00), followed by Furniture ($900.00) and Home ($712.81).   
Regional Performance: The East region generated the highest revenue ($1,157.50), closely followed by North ($1,077.50), West ($762.81), and South ($495.00).

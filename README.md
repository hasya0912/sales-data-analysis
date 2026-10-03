# 📊 Sales Data Analysis

## 📌 Project Overview

This project analyzes sales data using Python and provides business insights about products, customers, cities and monthly sales performance.

The project demonstrates a complete beginner-level data analytics workflow, including data generation, data cleaning, analysis, visualization and version control using Git and GitHub.

---

## 🎯 Project Objectives

The main objectives of this project are:

- Analyze total sales
- Calculate total quantity sold
- Calculate average order value
- Identify the best-selling product
- Identify the highest-performing city
- Identify top customers
- Analyze monthly sales trends
- Create useful data visualizations

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- Git
- GitHub

---

## 📂 Project Structure

```text
sales-data-analysis/
│
├── data/
│   └── sales_data.csv
│
├── notebooks/
│   └── sales_analysis.ipynb
│
├── images/
│   ├── monthly_sales.png
│   ├── product_sales.png
│   ├── city_sales.png
│   ├── top_customers.png
│   └── correlation_matrix.png
│
├── create_dataset.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 📊 Dataset

The dataset contains 300 sales transactions.

### Dataset columns

| Column     | Description         |
| ---------- | ------------------- |
| Order_ID   | Unique order number |
| Date       | Date of transaction |
| Customer   | Customer name       |
| City       | Customer city       |
| Product    | Product sold        |
| Quantity   | Quantity sold       |
| Unit_Price | Price per unit      |

A calculated `Sales` column is created during analysis:

```text
Sales = Quantity × Unit Price
```

---

## 🔍 Analysis Performed

The project performs:

### 1. Data Exploration

- Dataset shape
- Column information
- Data types
- Missing-value checking
- Statistical summary

### 2. Sales Analysis

- Total sales
- Total quantity
- Average order value
- Product-wise sales
- City-wise sales
- Customer-wise sales
- Monthly sales

### 3. Data Visualization

The project creates:

- Monthly sales chart
- Product sales chart
- City sales chart
- Top customer chart
- Correlation matrix

---

## 📈 Business Questions

This project answers questions such as:

1. What are the total sales?
2. Which product generates the highest sales?
3. Which city performs best?
4. Who are the top customers?
5. Which month has the highest sales?
6. What is the average order value?

---

## 🚀 How to Run the Project

### Step 1: Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Open the project

```bash
cd sales-data-analysis
```

### Step 3: Create a virtual environment

```bash
python -m venv venv
```

### Step 4: Activate the environment

Windows:

```bash
venv\Scripts\activate
```

### Step 5: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Run the dataset generator

```bash
python create_dataset.py
```

### Step 7: Open the notebook

Open:

```text
notebooks/sales_analysis.ipynb
```

Run the notebook cells from top to bottom.

---

## 📌 Key Skills Demonstrated

This project demonstrates:

- Data loading
- Data cleaning
- Data transformation
- Data aggregation
- GroupBy operations
- Business analysis
- Data visualization
- Python programming
- Git version control
- GitHub repository management

---

## 🔄 Git Workflow Used

The project uses the following Git workflow:

```text
Make changes
     ↓
git status
     ↓
git add .
     ↓
git commit
     ↓
git push
     ↓
GitHub
```

---

## 👨‍💻 Author

**Hasya Patel**

Data Analytics | Python | Pandas | Git | GitHub

import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

customers = [
    "ABC Traders",
    "Shree Sales",
    "Patel Hardware",
    "Jay Ambe Traders",
    "Krishna Enterprise",
    "Om Hardware",
    "Shivam Traders",
    "Arihant Sales",
    "Royal Hardware",
    "Mahalaxmi Enterprise",
    "Shakti Traders",
    "New Gujarat Sales",
    "Maruti Hardware",
    "Ganesh Traders",
    "Umiya Enterprise"
]

cities = [
    "Ahmedabad",
    "Surat",
    "Vadodara",
    "Rajkot",
    "Gandhinagar",
    "Mehsana",
    "Anand",
    "Nadiad"
]

products = {
    "Wall Putty": 500,
    "Primer": 650,
    "Wall Texture": 900,
    "Distemper": 450,
    "Exterior Paint": 1100
}

start_date = datetime(2026, 1, 1)

data = []

for i in range(1, 301):

    date = start_date + timedelta(days=random.randint(0, 273))

    product = random.choice(list(products.keys()))

    unit_price = products[product]

    quantity = random.randint(5, 50)

    customer = random.choice(customers)

    city = random.choice(cities)

    data.append([
        1000 + i,
        date.strftime("%Y-%m-%d"),
        customer,
        city,
        product,
        quantity,
        unit_price
    ])

df = pd.DataFrame(
    data,
    columns=[
        "Order_ID",
        "Date",
        "Customer",
        "City",
        "Product",
        "Quantity",
        "Unit_Price"
    ]
)

df.to_csv("data/sales_data.csv", index=False)

print("Dataset created successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))
print("\nFirst 5 rows:")
print(df.head())
import duckdb
import pandas as pd
import numpy as np

np.random.seed(42)
n = 5000

categories = ['Electronics', 'Furniture', 'Office Supplies', 'Apparel']
regions = ['North America', 'EMEA', 'APAC', 'LATAM']

data = {
    'order_id': [f"ORD-{10000 + i}" for i in range(n)],
    'order_date': pd.date_range(start='2025-01-01', periods=n, freq='h'),
    'category': np.random.choice(categories, size=n, p=[0.35, 0.25, 0.25, 0.15]),
    'region': np.random.choice(regions, size=n, p=[0.4, 0.3, 0.2, 0.1]),
    'revenue': np.round(np.random.exponential(scale=120, size=n) + 20, 2),
    'discount_pct': np.random.choice([0.0, 0.05, 0.10, 0.15, 0.25, 0.35], size=n, p=[0.4, 0.2, 0.15, 0.1, 0.1, 0.05])
}

df = pd.DataFrame(data)
cogs_ratio = {'Electronics': 0.62, 'Furniture': 0.70, 'Office Supplies': 0.45, 'Apparel': 0.40}
df['cogs'] = df.apply(lambda row: round(row['revenue'] * (cogs_ratio[row['category']] + np.random.uniform(-0.05, 0.05)), 2), axis=1)

con = duckdb.connect()
con.register('df_sales', df)
con.execute("COPY df_sales TO 'data/sales_sample.parquet' (FORMAT PARQUET)")
print("data/sales_sample.parquet generated successfully.")

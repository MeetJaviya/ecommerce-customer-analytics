import pandas as pd
# import numpy as np

df = pd.read_csv("data/processed/cleaned_data.csv")

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

snapshot = df['InvoiceDate'].max()

rfm = df.groupby('CustomerID').agg({

'InvoiceDate': lambda x: (snapshot - x.max()).days,
'InvoiceNo': 'count',
'TotalPrice': 'sum'

})

rfm.columns = ['Recency','Frequency','Monetary']

rfm['Churn'] = rfm['Recency'].apply(lambda x: 1 if x > 90 else 0)

# rfm['Churn'] = np.where(
#     (rfm['Recency'] > 90) & (rfm['Frequency'] < 3),
#     1,
#     0
# )

rfm.to_csv("data/processed/rfm_data.csv")
rfm.to_excel("excel/rfm.xlsx", index=False)


print("Feature Engineering Completed")

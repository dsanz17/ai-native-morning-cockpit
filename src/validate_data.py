import pandas as pd

from src.data_generator import generate_bank_history


df = generate_bank_history(months=48, seed=20260826)

print("\n--- DATASET CHECK ---")
print(f"Start date: {df.index.min():%Y-%m-%d}")
print(f"End date:   {df.index.max():%Y-%m-%d}")
print(f"Rows:       {len(df)}")

latest = df.iloc[-1]

print("\n--- LATEST RAW VALUES (EUR m) ---")
print(f"Loans:          {latest['loans']:,.0f}")
print(f"Deposits:       {latest['deposits']:,.0f}")
print(f"GCA:            {latest['gca']:,.0f}")
print(f"EAD:            {latest['ead']:,.0f}")
print(f"Provisions:     {latest['provisions']:,.0f}")
print(f"RWA:            {latest['rwa']:,.0f}")
print(f"CET1 capital:   {latest['cet1_capital']:,.0f}")
print(f"HQLA:           {latest['hqla']:,.0f}")
print(f"NII monthly:    {latest['nii']:,.0f}")
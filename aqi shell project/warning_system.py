import pandas as pd

# Load dataset
df = pd.read_csv("air_quality.csv")

print("Air Quality Warning System\n")

for i in range(len(df)):
    pm25 = df.loc[i, "pm2_5"]
    date = df.loc[i, "date"]

    if pm25 > 100:
        print(f"{date} ⚠️ WARNING: Air Quality is POOR!")
    elif pm25 > 60:
        print(f"{date} ⚠️ CAUTION: Air Quality is MODERATE")
    else:
        print(f"{date} ✅ Air Quality is GOOD")
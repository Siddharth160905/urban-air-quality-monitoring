import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("air_quality.csv")
# Display first rows
print(df.head())

# Average pollution values
avg_pollution = df[['pm2_5','pm10','no2','co']].mean()
print(avg_pollution)

# Plot PM2.5 trend
plt.plot(df['pm2_5'])
plt.title("PM2.5 Pollution Levels")
plt.xlabel("Time")
plt.ylabel("PM2.5")
plt.show()

import matplotlib.pyplot as plt

# Your existing data (example)
data = [
    ("2024-01-01", "GOOD"),
    ("2024-01-02", "MODERATE"),
    ("2024-01-03", "POOR")
]

dates = []
status_values = []

print("Air Quality Warning System\n")

for date, status in data:
    dates.append(date)

    if status == "GOOD":
        print(f"{date} ✅ Air Quality is GOOD")
        status_values.append(1)

    elif status == "MODERATE":
        print(f"{date} ⚠️ CAUTION: Air Quality is MODERATE")
        status_values.append(2)

    elif status == "POOR":
        print(f"{date} 🚨 WARNING: Air Quality is POOR!")
        status_values.append(3)

# 📊 Graph part (attach here)
plt.figure()

plt.plot(dates, status_values, marker='o')

plt.xlabel("Date")
plt.ylabel("Air Quality Level")
plt.title("Air Quality Warning System")

plt.yticks([1, 2, 3], ["GOOD", "MODERATE", "POOR"])

plt.grid()

plt.show()
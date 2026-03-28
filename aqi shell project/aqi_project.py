import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("air_quality.csv")

# Simple AQI calculation using PM2.5
def calculate_aqi(pm):
    if pm <= 50:
        return "Good"
    elif pm <= 100:
        return "Moderate"
    elif pm <= 150:
        return "Unhealthy for Sensitive Groups"
    elif pm <= 200:
        return "Unhealthy"
    else:
        return "Very Unhealthy"

df["AQI_Status"] = df["pm2_5"].apply(calculate_aqi)

print("Air Quality Data:\n")
print(df)

# Graph for PM2.5
plt.plot(df["pm2_5"])
plt.title("PM2.5 Pollution Trend")
plt.xlabel("Days")
plt.ylabel("PM2.5 Level")
plt.show()

# Graph for PM10
plt.plot(df["pm10"])
plt.title("PM10 Pollution Trend")
plt.xlabel("Days")
plt.ylabel("PM10 Level")
plt.show()
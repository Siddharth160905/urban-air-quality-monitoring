import matplotlib.pyplot as plt

# Step 1: Data (same as your output)
dates = ["2024-01-01", "2024-01-02", "2024-01-03"]
status = ["GOOD", "MODERATE", "POOR"]

# Step 2: Convert status to numeric values
status_values = []

for s in status:
    if s == "GOOD":
        status_values.append(1)
    elif s == "MODERATE":
        status_values.append(2)
    elif s == "POOR":
        status_values.append(3)

# Step 3: Create graph
plt.figure()

plt.plot(dates, status_values, marker='o')

# Labels and title
plt.xlabel("Date")
plt.ylabel("Air Quality Level")
plt.title("Air Quality Warning System")

# Custom Y-axis labels
plt.yticks([1, 2, 3], ["GOOD", "MODERATE", "POOR"])

# Grid
plt.grid()

# Show graph
plt.show()

colors = ["green", "orange", "red"]

plt.scatter(dates, status_values, c=colors, s=100)
plt.plot(dates, status_values)
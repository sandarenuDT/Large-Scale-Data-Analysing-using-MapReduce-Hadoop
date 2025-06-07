import matplotlib.pyplot as plt
import os

monthly_data = {}

with open('C:/Semester8/Cloud/Retail_map/Retail_map/output/result.txt', 'r') as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) == 2:
            month, count = parts
            if month.isalpha():
                monthly_data[month] = int(count)
#months dictionary
ordered_months = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]

# Filter and order the data
months = []
counts = []

for month in ordered_months:
    if month in monthly_data:
        months.append(month)
        counts.append(monthly_data[month])

# Plotting
plt.figure(figsize=(12, 6))
plt.bar(months, counts, color='coral')
plt.title('Monthly Transactions')
plt.xlabel('Month')
plt.ylabel('Number of Transactions')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Save the plot
output_path = 'C:/Semester8/Cloud/Retail_map/Retail_map/output/transactions_plot.png'
plt.savefig(output_path)
print(f"Plot saved to: {output_path}")

# Show the plot
plt.show()

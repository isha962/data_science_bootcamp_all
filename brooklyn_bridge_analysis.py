# brooklyn_bridge_analysis.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("Brooklyn_Bridge_Automated_Pedestrian_Counts_Demonstration_Project.csv")

# Check columns
print("Columns in dataset:\n", df.columns, "\n")

# Convert Date field to datetime
df['Date'] = pd.to_datetime(df['Date'])


df['DayOfWeek'] = df['Date'].dt.day_name()
weekday_df = df[df['DayOfWeek'].isin(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])]

# Group by weekday and sum pedestrian counts
weekday_counts = weekday_df.groupby('DayOfWeek')['Pedestrians'].sum().reindex(
    ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
)

# Plot weekday pedestrian counts
plt.figure(figsize=(8,5))
plt.plot(weekday_counts.index, weekday_counts.values, marker='o', linewidth=2)
plt.title('Pedestrian Counts (Weekdays Only)')
plt.xlabel('Day of Week')
plt.ylabel('Total Pedestrians')
plt.grid(True)
plt.tight_layout()
plt.show()


df_2019 = df[df['Date'].dt.year == 2019].copy()

# Drop rows with missing weather info
df_2019 = df_2019.dropna(subset=['Weather Summary'])

# Group by Weather Summary
weather_summary = df_2019.groupby('Weather Summary')['Pedestrians'].sum().sort_values(ascending=False)
print("\nTotal Pedestrians by Weather Summary (2019):\n", weather_summary)

# Correlation Matrix for numeric columns
corr_matrix = df_2019[['Pedestrians', 'Temperature (°F)', 'Humidity (%)']].corr()
print("\nCorrelation Matrix (2019):\n", corr_matrix)


def categorize_time_of_day(hour):
    if 5 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 17:
        return 'Afternoon'
    elif 17 <= hour < 21:
        return 'Evening'
    else:
        return 'Night'

# Extract hour and apply custom function
df['Hour'] = pd.to_datetime(df['Hour Beginning']).dt.hour
df['TimeOfDay'] = df['Hour'].apply(categorize_time_of_day)

# Analyze pedestrian activity by time of day
time_of_day_counts = df.groupby('TimeOfDay')['Pedestrians'].sum().reindex(
    ['Morning', 'Afternoon', 'Evening', 'Night']
)

plt.figure(figsize=(8,5))
plt.bar(time_of_day_counts.index, time_of_day_counts.values, color='skyblue', edgecolor='black')
plt.title('Pedestrian Activity by Time of Day')
plt.xlabel('Time of Day')
plt.ylabel('Total Pedestrians')
plt.tight_layout()
plt.show()

print("\nPedestrian Activity by Time of Day:\n", time_of_day_counts)

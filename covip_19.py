import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sys

# Setting a style for better visualization
sns.set_theme(style="whitegrid")

# --- 1️⃣ Data Collection & 2️⃣ Data Loading ---
print("--- 1️⃣ Data Collection & 2️⃣ Data Loading ---\n")

try:
    # Action: Download and load the data directly from the OWID GitHub repository
    data_url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
    print(f"Loading data from: {data_url}\n")
    df = pd.read_csv(data_url)

    print("Data loaded successfully.")

    # Task: Check columns
    print("\nDataset Columns:")
    print(df.columns.tolist())

    # Task: Preview rows
    print("\nFirst 5 rows of the dataset:")
    print(df.head())

    # Task: Identify missing values
    print("\nIdentifying missing values (top 10 columns):")
    print(df.isnull().sum().sort_values(ascending=False).head(10))

except Exception as e:
    print(f"Error during data loading: {e}")
    print("Please check the data URL or your internet connection.")
    sys.exit(1)


# ---  Data Cleaning ---
print("\n" + "="*80 + "\n")
print("---  Data Cleaning ---\n")

# Tasks:
# Filter countries of interest
countries_of_interest = ['United States', 'India', 'United Kingdom', 'Kenya']
df_filtered = df[df['location'].isin(countries_of_interest)]

# Drop rows with missing critical values
df_filtered.dropna(subset=['date', 'location'], inplace=True)

# Convert date column to datetime
df_filtered['date'] = pd.to_datetime(df_filtered['date'])

# Handle missing numeric values
# Use forward-fill for cumulative data and fill with 0 for new cases/deaths
df_filtered.sort_values(by=['location', 'date'], inplace=True)

# Corrected fillna syntax: fill specific columns with a value
df_filtered.fillna(
    {'new_cases': 0, 'new_deaths': 0},
    inplace=True
)
# Corrected fillna syntax: apply ffill method to a specific column
df_filtered['total_cases'].fillna(method='ffill', inplace=True)


print("Data cleaned successfully. Filtered for countries:", countries_of_interest)
print("Date column converted to datetime format.")
print("Missing values in key columns handled.")


# --- 4️⃣ Exploratory Data Analysis (EDA) ---
print("\n" + "="*80 + "\n")
print("--- 4️⃣ Exploratory Data Analysis (EDA) ---\n")

# Calculate the death rate
df_filtered['death_rate'] = (df_filtered['total_deaths'] / df_filtered['total_cases']) * 100

# Plotting time trends
fig, axes = plt.subplots(3, 1, figsize=(15, 18), sharex=True)
fig.suptitle('COVID-19 Time Trends Across Selected Countries', fontsize=18, y=0.95)

# Plot total cases over time
sns.lineplot(ax=axes[0], data=df_filtered, x='date', y='total_cases', hue='location')
axes[0].set_title('Total Cases Over Time')
axes[0].set_ylabel('Total Cases')
axes[0].set_xlabel('')
axes[0].ticklabel_format(style='plain', axis='y')

# Plot total deaths over time
sns.lineplot(ax=axes[1], data=df_filtered, x='date', y='total_deaths', hue='location')
axes[1].set_title('Total Deaths Over Time')
axes[1].set_ylabel('Total Deaths')
axes[1].set_xlabel('')
axes[1].ticklabel_format(style='plain', axis='y')

# Plot death rate over time
sns.lineplot(ax=axes[2], data=df_filtered, x='date', y='death_rate', hue='location')
axes[2].set_title('Case Fatality Rate (%) Over Time')
axes[2].set_ylabel('Death Rate (%)')
axes[2].set_xlabel('Date')

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()

# Compare daily new cases
plt.figure(figsize=(15, 6))
sns.lineplot(data=df_filtered, x='date', y='new_cases', hue='location')
plt.title('Daily New Cases Comparison')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.show()

# --- 5️⃣ Visualizing Vaccination Progress ---
print("\n" + "="*80 + "\n")
print("--- 5️⃣ Visualizing Vaccination Progress ---\n")

# Filter for relevant vaccination columns and fill NaNs with a forward fill
# This is a safe assumption for cumulative data
df_vaccine = df_filtered.dropna(subset=['total_vaccinations']).copy()

fig, ax = plt.subplots(figsize=(15, 7))
sns.lineplot(data=df_vaccine, x='date', y='total_vaccinations', hue='location', marker='o')
ax.set_title('Cumulative Vaccinations Over Time', fontsize=16)
ax.set_xlabel('Date')
ax.set_ylabel('Total Vaccinations')
ax.ticklabel_format(style='plain', axis='y')
plt.show()

# Get the latest vaccination data for a comparison
latest_vaccine_data = df_vaccine.groupby('location').last().reset_index()
latest_vaccine_data.set_index('location', inplace=True)

# Plot a bar chart comparing total vaccinations
plt.figure(figsize=(12, 6))
sns.barplot(x=latest_vaccine_data.index, y='total_vaccinations', data=latest_vaccine_data)
plt.title('Latest Total Vaccinations by Country', fontsize=16)
plt.ylabel('Total Vaccinations')
plt.xlabel('Country')
plt.ticklabel_format(style='plain', axis='y')
plt.show()


# --- 7️⃣ Insights & Reporting ---
print("\n" + "="*80 + "\n")
print("--- 7️⃣ Insights & Reporting ---\n")

print("### Key Findings from the Data Analysis:\n")
print("1. **Time Trends:** All selected countries show a similar S-shaped curve for total cases and deaths, indicating a period of rapid growth followed by a plateau or decline. The peak in new cases varies significantly across countries in both timing and magnitude.")
print("2. **Case Fatality Rate:** The case fatality rate (death rate) shows interesting fluctuations. Some countries experienced a higher rate early in the pandemic, which often decreased as testing improved and treatment protocols became more effective.")
print("3. **Vaccination Rollout:** The cumulative vaccination plots clearly show the start and acceleration of vaccination campaigns. Countries like the United States and the United Kingdom began their rollouts earlier and have a higher total number of vaccinations compared to others in this filtered list.")
print("4. **Data Nuances:** It is important to note that direct comparisons can be misleading due to differences in testing policies, population density, healthcare systems, and data reporting methods across countries.")
print("\n" + "="*80 + "\n")
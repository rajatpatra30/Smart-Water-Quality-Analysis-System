import pandas as pd
import matplotlib.pyplot as plt
# ====================================
# 1.Load Dataset
# ====================================
data = pd.read_csv("water_quality.csv")
print(data.head())

# ====================================
# 2. Data Cleaning
# ====================================
# Convert all columns to numeric
data = data.apply(pd.to_numeric,errors ='coerce')

# Fill missing valus with mean
data = data.fillna(data.mean(numeric_only=True))

# Basic statistics
print("\nStatistics:\n")
print(data.describe())

# =====================================
# 4. Water Quality Index(WQI)
# =====================================
data["WQI"] = (
    data["aluminium"]* 0.1 +
    data["ammonia"]* 0.1 +
    data["arsenic"]* 0.2 +
    data["nitrates"]* 0.2 +
    data["flouride"]* 0.2 +
    data["bacteria"]* 0.2 
)

print("\n=== WQI values ===\n")
print(data["WQI"].head())

# =====================================
# 4.Classification
# =====================================
def classify(wqi):
    if wqi < 50:
        return "Safe"
    elif wqi < 100:
        return "Moderate" 
    else:
        return "Unsafe" 
data["Quality"] = data["WQI"].apply(classify) 
print("\n===Water Quality Classification===\n") 

# ======================================
# 5.Find worst sample(high contamaintatio)
# ======================================
worst_index = data["WQI"].idxmax()
print("\n=== WOrst WAter Samplw ===\n")
print(data.loc[worst_index])

# ======================================
# 6.Top 5 polluted samples
# ======================================
top_polluted = data.sort_values(by="WQI",ascending=False).head(5)

print("\n=== Top 5 Most polluted samples ===\n")
print(top_polluted)

# ======================================
# 7. Visualization
# ======================================

# Graph 1: Aluminium distribution
plt.figure()
plt.hist(data["aluminium"],bins=20)
plt.title("Aluminium Distribution")
plt.xlabel("Aluminium")
plt.ylabel("Frequency")
plt.show()


# Graph 2: Nitrate vs Ammonia
plt.figure()
plt.scatter(data["nitrates"],data["ammonia"])
plt.title("Nitrate vs Ammonia")
plt.xlabel("Nitrate")
plt.ylabel("Ammonia")
plt.show()

# Graph 3: Water Quality Category
plt.figure()
data["Quality"].value_counts().plot(kind='bar')
plt.title("Water Quality Classification")
plt.xlabel("Category")
plt.ylabel("Count")
plt.show()

# ========================================
# 8. Save Processed Data
# ========================================
data.to_csv("processed_water_data.csv", index=False)

print("\nProcessed data saved as 'processed_water_data.csv'")

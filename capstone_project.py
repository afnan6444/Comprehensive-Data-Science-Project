

# -------------------------------
# Phase 1: Setup & Imports
# -------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import warnings
warnings.filterwarnings("ignore")

# -------------------------------
# Phase 2: Load & Inspect Data
# -------------------------------
# Replace with your dataset path
df = pd.read_csv("sales_data.csv")

print(df.head())
print(df.info())
print(df.describe())

# -------------------------------
# Phase 3: Data Preprocessing
# -------------------------------
# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Encode categorical variables
label_encoders = {}
for col in ['Product', 'Region', 'Customer_ID']:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Feature engineering
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year
df['Revenue'] = df['Quantity'] * df['Price']

# -------------------------------
# Phase 4: Exploratory Analysis
# -------------------------------
plt.figure(figsize=(10,6))
sns.lineplot(x="Date", y="Total_Sales", data=df)
plt.title("Sales Trend Over Time")
plt.show()

plt.figure(figsize=(8,5))
sns.barplot(x="Region", y="Total_Sales", data=df)
plt.title("Sales by Region")
plt.show()

# -------------------------------
# Phase 5: Model Development
# -------------------------------
# Define features and target
X = df[['Product','Quantity','Price','Customer_ID','Region','Month','Year']]
y = df['Total_Sales']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale numeric features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model
rf = RandomForestRegressor(random_state=42)
rf.fit(X_train_scaled, y_train)

# Predictions
y_pred = rf.predict(X_test_scaled)

# Evaluation
print("R2 Score:", r2_score(y_test, y_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))

# -------------------------------
# Phase 6: Deployment Prep
# -------------------------------
# Example: Save model for API deployment
import joblib
joblib.dump(rf, "sales_model.pkl")
joblib.dump(scaler, "scaler.pkl")

# -------------------------------
# Phase 7: Business Insights
# -------------------------------
# Feature importance
feat_importances = pd.Series(rf.feature_importances_, index=X.columns)
feat_importances.sort_values().plot(kind='barh', figsize=(8,6))
plt.title("Feature Importance in Sales Prediction")
plt.show()

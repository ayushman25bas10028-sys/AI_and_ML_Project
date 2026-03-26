import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# 1. Load the Airport Data
try:
    path = r'C:\Users\HP Z BOOK\Desktop\AI ML PROJECT\flight_data.csv'
    df = pd.read_csv(path)
except FileNotFoundError:
    print("Error: Could not find flight_data.csv!")
    exit()

# 2. Encode Categories (AI only understands numbers)
# We turn "Sunny" into 1, "Stormy" into 2, etc.
encoders = {}
for column in ['airline', 'weather', 'time_of_day']:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    encoders[column] = le

X = df[['airline', 'weather', 'time_of_day']]
y = df['status']

# 3. Use a Random Forest (Great for structured table data like this)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# 4. Prediction Function
def predict_flight(airline, weather, time):
    # Convert input strings to the numbers the AI learned
    input_data = pd.DataFrame([[
        encoders['airline'].transform([airline])[0],
        encoders['weather'].transform([weather])[0],
        encoders['time_of_day'].transform([time])[0]
    ]], columns=['airline', 'weather', 'time_of_day'])
    
    prediction = model.predict(input_data)[0]
    status_map = {0: "ON TIME ✅", 1: "DELAYED ⚠️", 2: "CANCELLED ❌"}
    
    print(f"--- Flight Report ---")
    print(f"Airline: {airline} | Weather: {weather} | Time: {time}")
    print(f"Predicted Status: {status_map[prediction]}\n")

# 5. Run some real-world scenarios
print(f"Model Accuracy: {model.score(X_test, y_test)*100:.0f}%\n")

predict_flight("Delta", "Sunny", "Morning")    # Should be On Time
predict_flight("United", "Stormy", "Evening")  # Should be Cancelled
predict_flight("Southwest", "Rainy", "Afternoon") # Should be Delayed
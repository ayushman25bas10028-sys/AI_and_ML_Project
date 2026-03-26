#  Aviation Delay Predictor: AI-Driven Flight Status System

##  Overview
The **Aviation Delay Predictor** is a machine learning solution designed to help airports and airlines anticipate flight disruptions before they happen. By analyzing historical patterns between specific airlines, weather conditions, and time slots, the system predicts whether a flight will be **On Time**, **Delayed**, or **Cancelled**. 

Instead of reactive management, this tool allows for proactive decision-making using a **Random Forest Classifier** to achieve high-accuracy results (approx. 90%+).

---

##  Problem Statement
The global aviation industry operates on complex schedules where a single morning delay can cascade into massive operational failures. Currently, many regional airports lack automated tools to synthesize categorical data (Weather, Carrier, Time) to provide high-confidence predictions. This results in reactive management, increased labor costs, and poor passenger experiences. This project aims to bridge that gap with a data-driven classification model.

---

##  Objectives
* **Data Transformation:** Successfully convert categorical flight variables into numerical formats via Label Encoding.
* **Pattern Recognition:** Utilize Random Forest algorithms to identify correlations between weather conditions and airline performance.
* **High Reliability:** Achieve a predictive accuracy of **>80%** on unseen test data.
* **Confidence Reporting:** Provide a mathematical probability score for every prediction to assist human decision-makers.

---

##  Features
* **Multi-Class Classification:** Categorizes flights into three distinct statuses (On Time, Delayed, Cancelled).
* **Categorical Intelligence:** Uses Label Encoding to process text-based data like "Stormy" or "Delta Airlines."
* **Confidence Scoring:** Provides a percentage-based probability score for every prediction.
* **Robust Logic:** Powered by an ensemble of 100 Decision Trees (Random Forest) to ensure stability.

---

##  Functional Requirements
* **FR1:** Ingest structured flight data from `.csv` files.
* **FR2:** Automatically encode string-based inputs (e.g., "Sunny") into machine-readable integers.
* **FR3:** Partition data into Training and Testing sets to prevent overfitting.
* **FR4:** Output predictions into one of three states: On Time (0), Delayed (1), or Cancelled (2).
* **FR5:** Provide sub-second inference speed for real-time use.

---

##  Tools & Libraries Used
* **Pandas:** Data manipulation and CSV handling.
* **Scikit-Learn:** Core ML framework (RandomForest, LabelEncoder, train_test_split).
* **NumPy:** High-speed mathematical array operations.

## Installation steps
* open the Python file consisting the model. (Delay_estimator.py) in any compiler of your choice.
* Make sure all the required libraries mentioned above.
* prepare the data folder (flight_data.csv)
* Save it in the same folder where the python file is saved. (IMPORTANT)
* Now Run the predictor

##  Instructions for Testing
* To verify the AI, check the output for these specific scenarios:
* On Time Scenario: Input Delta, Sunny, Morning -> Expected: ON TIME 
* Cancellation Scenario: Input United, Stormy, Evening -> Expected: CANCELLED 
* Delay Scenario: Input Southwest, Rainy, Afternoon -> Expected: DELAYED 

##  Troubleshooting the Installation
* "Python is not recognized": Ensure Python 3.10 or higher is installed and added to your system PATH.
* "File Not Found": Double-check that your flight_data.csv is inside the folder where the estimator file is present
* "ModuleNotFoundError": try running pip install pandas scikit-learn manually.

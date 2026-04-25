import csv
from find_s import train_find_s, predict

# Load dataset
data = []
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # skip header
    for row in reader:
        data.append(row)

# Train model
hypothesis = train_find_s(data)

print("\nFinal Hypothesis:")
print(hypothesis)

# Test prediction
print("\nEnter student details to predict:")

study = input("Study Hours (High/Medium/Low): ")
attendance = input("Attendance (Good/Average/Poor): ")
assignment = input("Assignments (Yes/No): ")

test = [study, attendance, assignment]

result = predict(hypothesis, test)

print("\nPrediction:", result)
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Function to generate a random user ID
def generate_user_id(length=8):
    return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=length))

# Function to create random timestamps
def generate_random_timestamps(start_date, end_date, n):
    start = datetime.strptime(start_date, "%m/%d/%Y")
    end = datetime.strptime(end_date, "%m/%d/%Y")
    generated_dates = [start + timedelta(seconds=random.randint(0, int((end - start).total_seconds()))) for _ in range(n)]
    return sorted(generated_dates)

# Generate data
num_records = 1000
datasets = np.random.randint(2, 7, num_records)
scenarios = np.random.randint(1, 4, num_records)
details = [f"r{datasets[i]}_{scenarios[i]}_{random.randint(1, 1000)}.csv" for i in range(num_records)]
users = [generate_user_id() for _ in range(num_records)]

# Generate random start and end times
start_times = generate_random_timestamps("01/01/2010", "12/31/2011", num_records)
end_times = [start_times[i] + timedelta(minutes=random.randint(1, 120)) for i in range(num_records)]  # End time is 1 to 120 minutes after start

# Create DataFrame
data = pd.DataFrame({
    'dataset': datasets,
    'scenario': scenarios,
    'details': details,
    'user': users,
    'start': start_times,
    'end': end_times
})

# Display first 10 records
print(data.head(10))

# Save to a CSV file
data.to_csv("data.csv", index=False)
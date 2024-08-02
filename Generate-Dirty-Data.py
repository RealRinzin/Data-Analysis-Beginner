import pandas as pd
import numpy as np
import random
from faker import Faker
fake = Faker()

# Set seed for reproducibility
random.seed(42)
np.random.seed(42)

# Define the number of rows
num_rows = 500

# Create sample data
data = {
    'ID': range(1, num_rows + 1),
    'Name': [fake.name() if i % 10 != 0 else None for i in range(1, num_rows + 1)],  # Missing values
    'Age': [random.choice([np.nan, random.randint(18, 90)]) for _ in range(num_rows)],  # Missing values and valid data
    'Email': [fake.email() if i % 5 != 0 else '' for i in range(1, num_rows + 1)],  # Invalid emails
    'Country': [fake.country() if i % 5 != 0 else '' for i in range(1, num_rows + 1)],  # Country
    'Salary': [round(random.uniform(30000, 120000), 2) for _ in range(num_rows)],  # Correct salaries
    'JoinDate': [pd.to_datetime(f'2024-{random.randint(1, 12)}-{random.randint(1, 28)}') if i % 15 != 0 else '2024-XX-XX' for i in range(num_rows)],  # Incorrect date format
    'IsActive': [random.choice([True, False]) for _ in range(num_rows)],  # Correct boolean values
    'Score': [random.choice([np.nan, random.randint(0, 100), 'invalid']) for _ in range(num_rows)]  # Mixed types (numeric and string)
}

# Create DataFrame
df = pd.DataFrame(data)

# Introduce additional data flaws
# 1. Introduce extra spaces in the Name field
df['Name'] = df['Name'].apply(lambda x: x + ' ' if x is not None else x)

# 2. Some Age values are out of the realistic range
df.loc[random.sample(range(num_rows), 5), 'Age'] = [200, -10, 'not_a_number', np.nan, np.nan]

# 3. Salary values as strings
df.loc[random.sample(range(num_rows), 5), 'Salary'] = ['not_a_number', '45000.50', np.nan, '60000', '']

# 4. JoinDate with invalid date entries
df.loc[random.sample(range(num_rows), 5), 'JoinDate'] = ['2024-13-01', '2024-04-31', 'not_a_date', None, '2024-06-40']

# 5. Email with different formats
df.loc[random.sample(range(num_rows), 5), 'Email'] = [None, 'user@com', 'user@.com', 'user@domain', 'plainaddress']

# Save the DataFrame to a CSV file
df.to_csv('dirty_data.csv', index=False)

print("Dirty data generated and saved to 'dirty_data.csv'.")

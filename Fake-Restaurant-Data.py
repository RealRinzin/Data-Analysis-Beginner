import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()

# Define number of rows
num_rows = 500

# Create lists to hold the data
names = []
emails = []
phone_numbers = []
visit_dates = []
total_bills = []
payment_methods = []
ratings = []
feedbacks = []

for _ in range(num_rows):
    names.append(fake.name())
    emails.append(fake.email())
    phone_numbers.append(fake.phone_number())
    
    # Introduce invalid date formats and missing values
    if random.choice([True, False]):
        visit_dates.append(fake.date_this_year().strftime('%Y-%m-%d'))
    else:
        visit_dates.append(random.choice([None, 'INVALID_DATE']))
    
    # Total bills with some invalid values and NA
    if random.choice([True, False]):
        total_bills.append(round(random.uniform(5.0, 500.0), 2))
    else:
        total_bills.append(random.choice([None, 'INVALID_AMOUNT', np.nan]))
    
    # Payment methods with some invalid and missing values
    payment_methods.append(random.choice(['Cash', 'Credit Card', 'Debit Card', None, 'INVALID_METHOD']))
    
    # Ratings with some invalid and out-of-range values
    if random.choice([True, False]):
        ratings.append(random.uniform(1, 5))
    else:
        ratings.append(random.choice([None, 'INVALID_RATING', 6.0, -1.0]))
    
    # Feedbacks with some missing values and invalid entries
    feedbacks.append(random.choice([fake.sentence(), None, 'INVALID_FEEDBACK']))

# Create DataFrame
data = pd.DataFrame({
    'Name': names,
    'Email': emails,
    'Phone Number': phone_numbers,
    'Visit Date': visit_dates,
    'Total Bill': total_bills,
    'Payment Method': payment_methods,
    'Rating': ratings,
    'Feedback': feedbacks
})

# Save DataFrame to a CSV file
data.to_csv('restaurant_customers_fake_data.csv', index=False)

print("Fake data generated and saved to 'restaurant_customers_fake_data.csv'")

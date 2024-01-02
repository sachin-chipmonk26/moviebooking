import random
import pandas as pd

# Load the bookings.csv file
bookings_df = pd.read_csv("bookings.csv")

# Get the number of rows in the bookings.csv file
num_rows = len(bookings_df)

# Select a random sample of 20% of the rows
test_df = bookings_df.sample(frac=0.2, random_state=42)

# Save the test.csv file
test_df.to_csv("bookings_test.csv")
